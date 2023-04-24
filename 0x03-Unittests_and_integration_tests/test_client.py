#!/usr/bin/env python3
"""Test for Client"""

import unittest
from unittest import TestCase, mock
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Class"""

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
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)
