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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test public repos"""
        mock_json.return_value = [{"name": "ALx"}, {"name": "TheRoom"}]
        client = GithubOrgClient("test_org")
        with patch('client.GithubOrgClient._public_repos_url',
               new_callable=PropertyMock,
               return_value="https://api.github.com/orgs/test/repos") as mock_public:
             self.assertEqual(GithubOrgClient('test').public_repos(),
                              [i["name"] for i in [{"name": "ALx"}, {"name": "TheRoom"}]])
             mock_public.assert_called_once()
             mock_json.assert_called_once_with("https://api.github.com/orgs/test/repos")
        
        
        