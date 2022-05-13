import time
import json
import pytest
from HomeWork_9.common_actions import CommonActions
from HomeWork_9.LocatorsApp import ScienceActions
from HomeWork_9.Api import ApiValidation

api = ApiValidation

file = 'data.json'
with open(file, 'r') as f:
    data = json.load(f)


@pytest.mark.crud
class TestCrudUser:
    USER_NAME = data['simple_user']['username']
    USER_PASSWORD = data['simple_user']['password']
    USER_FIRST_NAME = data['simple_user']['first_name']
    USER_LAST_NAME = data['simple_user']['last_name']
    USER_EMAIL = data['simple_user']['email']
    NEW_USER_NAME = data['simple_user']['new_username']

    @pytest.mark.usefixtures('docker')
    def test_create_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.USER_NAME)
        assert check_user_result is False, 'This user already exists'
        driver = driver_setup
        ca = CommonActions()
        ca.login_to_the_resource_as_admin(driver)
        science_actions = ScienceActions(driver)
        science_actions.click_add_user_button()
        science_actions.enter_username_for_creating_user(self.USER_NAME)
        science_actions.enter_password_for_creating_user(self.USER_PASSWORD)
        science_actions.enter_confirm_password_for_creating_user(self.USER_PASSWORD)
        science_actions.click_save_creating_user()
        check_message = science_actions.get_text_from_success_message()
        time.sleep(3)
        assert check_message == f'The user “{self.USER_NAME}” was added successfully. You may edit it again below.'

    @pytest.mark.usefixtures('docker')
    def test_read_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.USER_NAME)
        assert check_user_result is True, 'This user does not exist'
        driver = driver_setup
        ca = CommonActions()
        science_actions = ScienceActions(driver)
        ca.login_to_the_resource_as_a_user(driver, self.USER_NAME, self.USER_PASSWORD)
        check_logged_in_user_name = science_actions.get_text_from_dropdown()
        assert check_logged_in_user_name == self.USER_NAME

    @pytest.mark.usefixtures('docker')
    def test_update_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.USER_NAME)
        assert check_user_result is True, 'This user does not exist'
        driver = driver_setup
        ca = CommonActions()
        science_actions = ScienceActions(driver)
        ca.login_to_the_resource_as_admin(driver)
        science_actions.click_users_button()
        ca.search_the_user(driver, self.USER_NAME)
        science_actions.select_first_user_after_search()
        science_actions.change_username(self.NEW_USER_NAME)
        science_actions.enter_personal_info(self.USER_FIRST_NAME, self.USER_LAST_NAME, self.USER_EMAIL)
        science_actions.click_save_updating_user()
        check_change_success_message = science_actions.get_text_from_success_message()
        assert check_change_success_message == f'The user “{self.NEW_USER_NAME}” was changed successfully.'
        ca.search_the_user(driver, self.NEW_USER_NAME)
        check_email = science_actions.get_text_email_from_users_list()
        check_first_name = science_actions.get_text_first_name_from_users_list()
        check_last_name = science_actions.get_text_last_from_users_list()
        assert check_email == self.USER_EMAIL
        assert check_first_name == self.USER_FIRST_NAME
        assert check_last_name == self.USER_LAST_NAME

    @pytest.mark.usefixtures('docker')
    def test_delete_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.NEW_USER_NAME)
        assert check_user_result is True, 'This user does not exist'
        driver = driver_setup
        ca = CommonActions()
        science_actions = ScienceActions(driver)
        ca.login_to_the_resource_as_admin(driver)
        science_actions.click_users_button()
        ca.search_the_user(driver, self.NEW_USER_NAME)
        science_actions.select_first_user_after_search()
        science_actions.click_delete_button()
        check_sure_message = science_actions.get_text_confirm_delete_message()
        assert check_sure_message == f'Are you sure you want to delete the user "{self.NEW_USER_NAME}"? All of the ' \
                                     f'following related items will be deleted:'
        science_actions.click_confirm_delete_button()
        check_success_delete_message = science_actions.get_text_from_success_message()
        assert check_success_delete_message == f'The user “{self.NEW_USER_NAME}” was deleted successfully.'
