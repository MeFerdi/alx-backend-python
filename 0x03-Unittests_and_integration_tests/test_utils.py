#!/usr/bin/env python3
"""Unit tests for utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """Test that access_nested_map raises KeyError with correct message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        self.assertEqual(str(context.exception), expected_message)
class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result without making HTTP calls"""
        
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        # Call the function
        result = get_json(test_url)
        
        # Assert that requests.get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)
        
        # Assert that the result equals test_payload
        
        self.assertEqual(result, test_payload)
class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""
    
    def test_memoize(self):
        """Test that memoize decorator caches the result"""
        
        class TestClass:
            """Test class with memoized property"""
            
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()
            
        # Create instance and mock the a_method
        test_instance = TestClass()
        
        with patch.object(test_instance, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            
            # Assert results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            
            # Assert a_method was called only once
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()