import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()
username = os.environ['GH_USERNAME']
token = os.environ['GH_TOKEN']

BASE_URL = 'https://api.github.com'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}


def create_repo(repo_name, private, description):
    url = BASE_URL + '/user/repos'
    data = {
        'name': repo_name,
        'description': description,
        'private': private,
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 201:
        print('Successfully created repository')
        print(response.json()['html_url'])
    else:
        print('Failed to create repository')
        print('Response:', response.status_code, response.text)


def add_collaborator(email, repo):
    url = BASE_URL + f'/repos/{username}/{repo}/collaborators/{email}'
    print(url)
    data = {
        'permission': 'push'
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f'{email} Invitation sent to the collaborator.')
    elif response.status_code == 204:
        print('The user is already a collaborator.')
    else:
        print(f'{email} Failed to add collaborator.')
        print('Response:', response.status_code, response.text)


if __name__ == '__main__':

    repo_name = 'NewRepositoryName'
    description = 'Repo created by automation'
    private = True  # or False
    collaborators = ['username1', 'username2']
    create_repo(repo_name, private, description)
    for email in collaborators:
        add_collaborator(email, repo_name)
