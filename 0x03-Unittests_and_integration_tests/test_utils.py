#!/usr/bin/env python3
"""
This module contains unit tests for the utils module.
The utils module provides various utility functions that are used throughout
the project.These tests ensure that the functions in the utils module behave
as expected and do not introduce any regressions.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from typing import Dict


class TestAccessNestedMap(unittest.TestCase):
    """
    Accesses a nested value in a dictionary using a sequence of keys.

    Args:
        nested_map (dict): A dictionary with nested values.
        path (tuple): A sequence of keys to access the nested value.

    Returns:
        The value at the end of the path.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test function to check if the access_nested_map function returns
        the expected value.

        Args:
        - nested_map: A dictionary representing a nested map.
        - path: A list of keys representing the path to a value
        - expected: The expected value at the end of the path.

        Returns:
        - None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """
        Test that accessing a nested map raises the expected exception.

        Args:
            nested_map (dict): The nested map to access.
            path (list): The path to the value to access.
            exception (Exception): The expected exception to be raised.

        Raises:
            AssertionError: If the expected exception is not raised.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class for the `get_json` function.

    This class contains unit tests for the `get_json` function, which retrieves
    JSON data from a given URL using the `requests` library.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test the get_json function.

        Args:
            test_url (str): The URL to test.
            test_payload (dict): The expected payload.

        Returns:
            None
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """class to tests the memoize function"""
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
