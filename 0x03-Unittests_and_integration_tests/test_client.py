#!/usr/bin/env python3
"""Test for github class Client unit test"""

import unittest
from unittest import TestCase, mock
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import PropertyMock
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test Githuborg Class unittest"""

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """Test Org method for testinf"""
        url = f'https://api.github.com/orgs/{org_name}'
        client = GithubOrgClient(org_name)
        client.org()
        mock_get.assert_called_once_with(url)

    @patch.object(GithubOrgClient, "org", new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos_url(self, mock_org):
        """TEst public repos url"""
        url = "https://api.github.com/orgs/test_org/repos"
        mock_org.return_value = {"repos_url": url}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test public repos"""
        url = "https://api.github.com/orgs/test/repos"
        mock_json.return_value = [{"name": "ALx"}, {"name": "TheRoom"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock, return_value=url) as mock_public:
            self.assertEqual(GithubOrgClient('test').public_repos(),
                             [i["name"] for i in [{"name": "ALx"},
                                                  {"name": "TheRoom"}]])
            mock_public.assert_called_once()
            mock_json.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has license"""
        client = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {'org_payload': org_payload, 'repos_payload': repos_payload,
     'expected_repos': expected_repos, 'apache2_repos': apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test Integration Class for githuborgclient"""
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        self.mock_get.side_effect = [
            self.org_payload, self.repos_payload
        ]
        client = GithubOrgClient('google')
        repos = client.public_repos()

        self.assertListEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        self.mock_get.side_effect = [
            self.org_payload, self.repos_payload, self.apache2_repos
        ]
        client = GithubOrgClient('google')
        repos = client.public_repos('apache-2.0')

        self.assertListEqual(repos, self.apache2_repos)
