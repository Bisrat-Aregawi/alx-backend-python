#!/usr/bin/env python3
"""
Defines test class
"""
from parameterized import parameterized
from typing import Any, Mapping, Sequence
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Test class for test cases written for the function
    `access_nested_map
    """
    def setUp(self) -> None:
        """Import and make available the method `access_nested_map`
        """
        from utils import access_nested_map
        self.access_nested_map = access_nested_map

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(
            self, mapping: Mapping, sequence: Sequence, root: Any
            ) -> None:
        """Test `access_nested_map` function
        """
        self.assertEqual(self.access_nested_map(mapping, sequence), root)

    def tearDown(self) -> None:
        """Delete unused reference to the function `access_nested_map`
        """
        del self.access_nested_map
    pass
