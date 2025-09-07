#!/usr/bin/env python3
"""Unit tests for client module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""
    
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value"""
        test_payload = {"login": org_name, "id": 12345}
        mock_get_json.return_value = test_payload
        
        client = GithubOrgClient(org_name)
        result = client.org
        
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, test_payload)
    
    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct value"""
        # Test payload with repos_url
        test_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        
        # Mock the org property to return our test payload
        with patch('client.GithubOrgClient.org', 
                  new_callable=PropertyMock) as mock_org:
            # Set the return value to the actual dictionary
            mock_org.return_value = test_payload
            
            # Create client instance
            client = GithubOrgClient("testorg")
            
            # Call the _public_repos_url property
            result = client._public_repos_url
            
            # Assert the result is correct
            self.assertEqual(result, test_payload["repos_url"])
            
            # Verify the org property was accessed
            mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()