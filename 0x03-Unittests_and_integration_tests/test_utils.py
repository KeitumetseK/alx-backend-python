import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

# Test class for GithubOrgClient
@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()
        mock_get.side_effect = lambda url: Mock(json=lambda: cls.org_payload if "orgs" in url else cls.repos_payload)

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json, mock_public_repos_url):
        # Mock _public_repos_url to return a specific URL
        mock_public_repos_url.return_value = "http://example.com/repos"
        # Mock get_json to return repos filtered by license
        mock_get_json.return_value = self.apache2_repos
        
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)
        
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://example.com/repos?license=apache-2.0")


