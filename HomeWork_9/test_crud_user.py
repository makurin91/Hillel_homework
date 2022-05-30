import time
import pytest
from HomeWork_9.common_actions import CommonActions
from HomeWork_9.locators_app import ScienceActions
from HomeWork_9.api import ApiValidation
import logging

api = ApiValidation
LOGGER = logging.getLogger(__name__)


@pytest.mark.crud
@pytest.mark.usefixtures('read_data_file')
class TestCrudUser:

    # def setup(self):
    #     api = ApiValidation
    #     check_user_result = api.check_user_exists(self.USER_NAME, self.USERS_ENDPOINT, self.ADM_USERNAME,
    #                                               self.ADM_PASSWORD)
    #     return check_user_result

    @pytest.mark.cd
    @pytest.mark.usefixtures('docker')
    def test_create_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.USER_NAME, self.USERS_ENDPOINT, self.ADM_USERNAME,
                                                  self.ADM_PASSWORD)
        assert check_user_result is False, LOGGER.error('This user already exists')
        driver = driver_setup
        ca = CommonActions()
        LOGGER.info('Login to the admin panel')
        ca.login_to_the_resource_as_admin(driver, self.ADMIN_URL, self.ADM_USERNAME, self.ADM_PASSWORD)
        science_actions = ScienceActions(driver)
        LOGGER.info('Click "Add user" button and enter credentials of the new user')
        science_actions.click_add_user_button()
        science_actions.enter_username_for_creating_user(self.USER_NAME)
        science_actions.enter_password_for_creating_user(self.USER_PASSWORD)
        science_actions.enter_confirm_password_for_creating_user(self.USER_PASSWORD)
        LOGGER.info('Click "save" button')
        science_actions.click_save_creating_user()
        check_message = science_actions.get_text_from_success_message()
        time.sleep(3)
        LOGGER.info('Check the message about creating user')
        assert check_message == f'The user “{self.USER_NAME}” was added successfully. You may edit it again below.',\
            LOGGER.error(f'message "{check_message}" is not shown or {self.USER_NAME} is wrong')

    @pytest.mark.usefixtures('docker')
    def test_read_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.USER_NAME, self.USERS_ENDPOINT, self.ADM_USERNAME,
                                                  self.ADM_PASSWORD)
        assert check_user_result is True, 'This user does not exist'
        driver = driver_setup
        ca = CommonActions()
        science_actions = ScienceActions(driver)
        ca.login_to_the_resource_as_a_user(driver, self.USER_URL, self.USER_NAME, self.USER_PASSWORD)
        check_logged_in_user_name = science_actions.get_text_from_dropdown()
        assert check_logged_in_user_name == self.USER_NAME

    @pytest.mark.usefixtures('docker')
    def test_update_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.USER_NAME, self.USERS_ENDPOINT, self.ADM_USERNAME,
                                                  self.ADM_PASSWORD)
        assert check_user_result is True, 'This user does not exist'
        driver = driver_setup
        ca = CommonActions()
        science_actions = ScienceActions(driver)
        ca.login_to_the_resource_as_admin(driver, self.ADMIN_URL, self.ADM_USERNAME, self.ADM_PASSWORD)
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
        science_actions.select_first_user_after_search()
        science_actions.change_username(self.USER_NAME)
        science_actions.click_save_updating_user()
        time.sleep(0.5)
        assert check_user_result is True, 'This user does not exist'

    @pytest.mark.cd
    @pytest.mark.usefixtures('docker')
    def test_delete_user(self, driver_setup):
        check_user_result = api.check_user_exists(self.USER_NAME, self.USERS_ENDPOINT, self.ADM_USERNAME,
                                                  self.ADM_PASSWORD)
        assert check_user_result is True, 'This user does not exist'
        driver = driver_setup
        ca = CommonActions()
        science_actions = ScienceActions(driver)
        ca.login_to_the_resource_as_admin(driver, self.ADMIN_URL, self.ADM_USERNAME, self.ADM_PASSWORD)
        science_actions.click_users_button()
        ca.search_the_user(driver, self.USER_NAME)
        science_actions.select_first_user_after_search()
        science_actions.click_delete_button()
        check_sure_message = science_actions.get_text_confirm_delete_message()
        assert check_sure_message == f'Are you sure you want to delete the user "{self.USER_NAME}"? All of the ' \
                                     f'following related items will be deleted:'
        science_actions.click_confirm_delete_button()
        check_success_delete_message = science_actions.get_text_from_success_message()
        assert check_success_delete_message == f'The user “{self.USER_NAME}” was deleted successfully.'
