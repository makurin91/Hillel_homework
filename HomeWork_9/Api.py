import requests
import pytest
import json

file = 'data.json'
with open(file, 'r') as f:
    data = json.load(f)


class ApiValidation:
    ADM_USERNAME = data['admin_user']['username']
    ADM_PASSWORD = data['admin_user']['password']
    user_path = data['api']['user_path']

    @staticmethod
    def check_user_exists(username, url=user_path, adm_username=ADM_USERNAME, adm_password=ADM_PASSWORD):
        resp = requests.get(url, auth=(adm_username, adm_password))
        resp_data = resp.json()
        for x in resp_data['results']:
            if x['username'] == f'{username}':
                return True
            return False
