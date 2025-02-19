import unittest
from unittest.mock import patch
from mastodon_service import create_post, retrieve_post, delete_post

class TestMastodonService(unittest.TestCase):

    @patch('requests.post')
    def test_create_post(self, mock_post):
        mock_post.return_value.json.return_value = {'id': '12345'}
        response = create_post('Hello, Mastodon!')
        self.assertEqual(response['id'], '12345')

    @patch('requests.get')
    def test_retrieve_post(self, mock_get):
        mock_get.return_value.json.return_value = {'id': '12345', 'content': 'Hello, Mastodon!'}
        response = retrieve_post('12345')
        self.assertEqual(response['id'], '12345')
        self.assertEqual(response['content'], 'Hello, Mastodon!')

    @patch('requests.delete')
    def test_delete_post(self, mock_delete):
        mock_delete.return_value.status_code = 200
        status_code = delete_post('12345')
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()