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
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test_org/repos")

    @patch('client.get_json',
       return_value={'repos_url': 'https://api.github.com/repos/octocat/Hello-World'})
    def test_public_repos(self, get_json_mock):
        """Test GithubOrgClient.public_repos"""

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as repos_url_mock:
            repos_url_mock.return_value = 'https://api.github.com/repos/octocat/Hello-World'
            client = GithubOrgClient('example')
            repos = client.public_repos()
            get_json_mock.assert_called_once_with('https://api.github.com/repos/octocat/Hello-World')
            repos_url_mock.assert_called_once()
            expected_repos = ['Hello-World']
            self.assertEqual(repos, expected_repos)