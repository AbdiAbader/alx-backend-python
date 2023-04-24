#!/usr/bin/env python3
"""Test class for utils"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),

    ])
   
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test access_nested_map exception"""
        self.assertRaisesRegex(KeyError, expected_key, access_nested_map, nested_map, path)