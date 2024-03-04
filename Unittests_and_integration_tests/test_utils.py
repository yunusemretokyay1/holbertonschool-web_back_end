#!/usr/bin/env python3
""" Module for testing utils """

from parameterized import parameterized
import unittest
from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for testing
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
