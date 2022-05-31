import requests
import pytest
from homework_9_10.checker import ApiValidation
import logging

api_checker = ApiValidation
LOGGER = logging.getLogger(__name__)


@pytest.mark.usefixtures('read_data_file')
class TestApiCrudUsers:
    cache = []

    def setup(self):
        self.check_exist = api_checker.check_user_exists(self.USER_NAME,
                                                         self.USERS_ENDPOINT, self.ADM_USERNAME, self.ADM_PASSWORD)
        self.payload_data = {
            "username": f"{self.USER_NAME}",
            "email": f"{self.USER_EMAIL}"
        }
        self.url = f"{self.USERS_ENDPOINT}"
        self.auth = (self.ADM_USERNAME, self.ADM_PASSWORD)
        self.update_pl_daya = {
            "username": f"{self.NEW_USER_NAME}"
        }

    def test_create_user_api(self):
        assert self.check_exist is False, LOGGER.error('This user already exists')
        response = requests.post(self.url, self.payload_data, auth=self.auth)
        assert response.status_code == 201
        user_id = response.json()['url'].split('/')[4]
        self.cache.append(user_id+'/')

    def test_read_user_api(self):
        LOGGER.info(self.cache[0])
        assert self.check_exist is True, LOGGER.error('This user does not exist')
        response = requests.get(self.url + self.cache[0], auth=self.auth)
        assert response.status_code == 200
        assert response.json()['username'] == self.USER_NAME, LOGGER.error('Wrong username')

    def test_update_user_api(self):
        assert self.check_exist is True, LOGGER.error('This user does not exist')
        response = requests.put(self.url + self.cache[0], self.update_pl_daya, auth=self.auth)
        assert response.status_code == 200
        assert response.json()['username'] == self.NEW_USER_NAME, LOGGER.error('Wrong username')
        requests.put(self.url + self.cache[0], self.payload_data, auth=self.auth)

    def test_delete_user_api(self):
        assert self.check_exist is True, LOGGER.error('This user does not exist')
        response = requests.delete(self.url + self.cache[0], auth=self.auth)
        assert response.status_code == 204
