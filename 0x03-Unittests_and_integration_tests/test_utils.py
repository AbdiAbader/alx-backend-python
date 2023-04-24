import unittest
from parameterized import parameterized
from access_nested_map import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def TestAccessNestedMap(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
