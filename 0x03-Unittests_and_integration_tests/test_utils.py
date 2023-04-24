#!/usr/bin/env python3
"""Test class for utils"""


import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import Mock, patch
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test Accessnestedmap"""

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

        self.assertRaisesRegex(KeyError, expected_key,
                               access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """TEST GET JSON"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])


    def test_get_json(self, url, payload):
        """Test get_json function"""
        mock = Mock()
        mock.json.return_value = payload
        with patch('requests.get', return_value=mock):
            result = get_json(url)
            self.assertEqual(result, payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """tEst for Memomize"""

    def test_memoize(self):
        """test memoize method"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)
            mock_method.assert_called_once()
