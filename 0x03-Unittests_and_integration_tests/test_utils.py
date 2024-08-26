#!/usr/bin/env python3

"""
Test suite for the GithubOrgClient class in the client module.

This module contains unit tests for the methods in the GithubOrgClient class,
including tests for public repositories and repository license filtering.
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestGithubOrgClient(unittest.TestCase):
    """
    Unit test class for GithubOrgClient.

    This class tests the functionality of the GithubOrgClient class, including
    fetching public repositories and filtering by license.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the test environment before running the tests.

        This method patches the `requests.get` function to return mock data
        based on the URL being queried.
        """
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()
        mock_get.side_effect = lambda url: Mock(json=lambda: cls.org_payload if "orgs" in url else cls.repos_payload)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Tear down the test environment after running the tests.

        This method stops the patching of `requests.get`.
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Test the public_repos method of GithubOrgClient.

        This test ensures that the public_repos method returns the expected
        list of repositories based on the mocked data.
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json: Mock, mock_public_repos_url: PropertyMock) -> None:
        """
        Test the public_repos method of GithubOrgClient with a license filter.

        This test ensures that the public_repos method, when passed a license
        filter, returns the expected list of repositories based on the mocked
        data.
        
        Args:
            mock_get_json (Mock): Mock of the get_json function.
            mock_public_repos_url (PropertyMock): Mock of the _public_repos_url property.
        """
        mock_public_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = self.apache2_repos
        
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)
        
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://example.com/repos?license=apache-2.0")


