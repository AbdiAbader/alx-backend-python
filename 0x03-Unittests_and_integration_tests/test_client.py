#!/usr/bin/env python3
"""Test for Client"""

import unittest
from unittest import TestCase, mock
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Class"""

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """Test Org method for testinf"""
        url = 'https://api.github.com/orgs/{org_name}'
        client = GithubOrgClient(org_name)
        client.org()
        mock_get.assert_called_once_with(url)
