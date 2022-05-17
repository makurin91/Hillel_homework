import requests


class ApiValidation:

    @staticmethod
    def check_user_exists(username, url, adm_username, adm_password):
        resp = requests.get(url, auth=(adm_username, adm_password))
        resp_data = resp.json()
        for x in resp_data['results']:
            if x['username'] == f'{username}':
                return True
            return False
