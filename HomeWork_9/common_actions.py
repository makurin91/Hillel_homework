import json
import pytest
from HomeWork_9.LocatorsApp import MyLocators
from HomeWork_9.LocatorsApp import ScienceActions

locators_list = MyLocators()

file = 'data.json'
with open(file, 'r') as f:
    data = json.load(f)


@pytest.mark.usefixtures('read_data_file')
class CommonActions:
    user_URL = data['resources']['user_url']
    admin_URL = data['resources']['admin_url']
    ADM_USERNAME = data['admin_user']['username']
    ADM_PASSWORD = data['admin_user']['password']

    def login_to_the_resource_as_admin(self, driver):
        """
        Login to the 'science' as a admin
        :param driver:
        :return:
        """
        driver.get(self.admin_URL)
        s_actions = ScienceActions(driver)
        s_actions.enter_username_for_login(self.ADM_USERNAME)
        s_actions.enter_password_for_login(self.ADM_PASSWORD)
        s_actions.click_login_button_at_admin_panel()

    def login_to_the_resource_as_a_user(self, driver, username, password):
        """
        Login to the 'science' as a user
        :param driver: Set a webdriver
        :param username: Set valid username
        :param password: Set valid password
        :return:
        """
        driver.get(self.user_URL)
        s_actions = ScienceActions(driver)
        s_actions.click_login_button_at_user_dashboard()
        s_actions.enter_username_for_login(username)
        s_actions.enter_password_for_login(password)
        s_actions.click_login_button_at_admin_panel()

    def search_the_user(self, driver, username):
        """
        Searching the user
        :param driver: Set webdriver
        :param username: Set user which will be found
        :return:
        """
        s_actions = ScienceActions(driver)
        s_actions.enter_user_for_search(username)
        s_actions.click_search()
