import requests
import pytest
from homework_9_10.checker import ApiValidation
import logging


@pytest.mark.api_crud
@pytest.mark.usefixtures('read_data_file')
class TestApiCrudUsers:

    def setup(self):
        self.check_exist = ApiValidation.check_user_exists(self.USER_NAME, self.USERS_ENDPOINT,
                                                           self.ADM_USERNAME, self.ADM_PASSWORD)
        self.payload_data = {
            "username": f"{self.USER_NAME}",
            "email": f"{self.USER_EMAIL}"
        }
        self.url = f"{self.USERS_ENDPOINT}"
        self.auth = (self.ADM_USERNAME, self.ADM_PASSWORD)
        self.update_pl_data = {
            "username": f"{self.NEW_USER_NAME}"
        }

    def setup_class(self):
        self.cache = []
        self.LOGGER = logging.getLogger(__name__)

    def test_create_user_api(self):
        assert self.check_exist is False, self.LOGGER.error('This user already exists')
        self.LOGGER.info(f'Created user with username {self.USER_NAME}')
        response = requests.post(self.url, self.payload_data, auth=self.auth)
        assert response.status_code == 201
        user_id = response.json()['url'].split('/')[4]
        self.cache.append(user_id + '/')

    def test_read_user_api(self):
        assert self.check_exist is True, self.LOGGER.error('This user does not exist')
        self.LOGGER.info(f'Read user with ID - {self.cache[0]}')
        response = requests.get(self.url + self.cache[0], auth=self.auth)
        assert response.status_code == 200
        assert response.json()['username'] == self.USER_NAME, self.LOGGER.error('Wrong username')

    def test_update_user_api(self):
        assert self.check_exist is True, self.LOGGER.error('This user does not exist')
        self.LOGGER.info(f'Update the name "{self.USER_NAME}" on the "{self.NEW_USER_NAME}"')
        response = requests.put(self.url + self.cache[0], self.update_pl_data, auth=self.auth)
        assert response.status_code == 200
        assert response.json()['username'] == self.NEW_USER_NAME, self.LOGGER.error('Wrong username')
        requests.put(self.url + self.cache[0], self.payload_data, auth=self.auth)

    def test_delete_user_api(self):
        assert self.check_exist is True, self.LOGGER.error('This user does not exist')
        self.LOGGER.info(f'Delete the user with name {self.USER_NAME}')
        response = requests.delete(self.url + self.cache[0], auth=self.auth)
        assert response.status_code == 204
