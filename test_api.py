import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_USER = os.environ.get('GITHUB_USER')
GITHUB_REPO = os.environ.get('GITHUB_REPO')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')


def test_create_repo():
    headers = {
        'Authorization': 'Bearer ' + GITHUB_TOKEN,
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28',
    }
    new_repo_response = requests.post('https://api.github.com/user/repos', headers=headers, json={
        'name': GITHUB_REPO,
    })
    assert new_repo_response.status_code == 201
    repo_list_response = requests.get(f'https://api.github.com/users/{GITHUB_USER}/repos')
    repo_name_list = {repo['name'] for repo in repo_list_response.json()}
    assert GITHUB_REPO in repo_name_list
    delete_repo_response = requests.delete(f'https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}', headers=headers)
    assert delete_repo_response.status_code == 204
