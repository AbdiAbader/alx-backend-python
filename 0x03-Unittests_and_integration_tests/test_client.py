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

    @mock.patch('client.get_json')
    @mock.patch.object(GithubOrgClient, '_public_repos_url', new_callable=mock.PropertyMock)
    def test_public_repos(self, org_name, repo_names, mock_url, mock_get_json):
        mock_url.return_value = f'https://api.github.com/orgs/{org_name}/repos'
        mock_get_json.return_value = [
            {'name': 'chromium', 'license': {'key': 'mit'}},
        ]
        client = GithubOrgClient(org_name)
        repos = client.public_repos('mit')
        self.assertEqual(repos, repo_names)
        mock_url.assert_called_once()
        mock_get_json.assert_called_once()
    
    