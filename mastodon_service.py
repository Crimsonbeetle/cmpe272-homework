import os
from dotenv import load_dotenv
import requests
# Deven Desai have contributed for below part of the code.
# Load environment variables from .env file
load_dotenv()

# Retrieve the access token from environment variables
access_token = os.getenv('MASTODON_ACCESS_TOKEN')

def create_post(content):
    url = 'https://mastodon.social/api/v1/statuses'
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {'status': content}
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating post: {e}")
        return None

def retrieve_post(post_id):
    url = f'https://mastodon.social/api/v1/statuses/{post_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving post: {e}")
        return None

def delete_post(post_id):
    url = f'https://mastodon.social/api/v1/statuses/{post_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error deleting post: {e}")
        return None

# Example usage
response = create_post("Hello, Mastodon!")
if response:
    print(response)