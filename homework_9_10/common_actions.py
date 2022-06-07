from homework_9_10.locators_app import ScienceActions


class CommonActions:

    def login_to_the_resource_as_admin(self, driver, admin_url, admin_username, admin_password):
        driver.get(admin_url)
        s_actions = ScienceActions(driver)
        s_actions.enter_username_for_login(admin_username)
        s_actions.enter_password_for_login(admin_password)
        s_actions.click_login_button_at_admin_panel()

    def login_to_the_resource_as_a_user(self, driver, user_url, username, password):
        driver.get(user_url)
        s_actions = ScienceActions(driver)
        s_actions.click_login_button_at_user_dashboard()
        s_actions.enter_username_for_login(username)
        s_actions.enter_password_for_login(password)
        s_actions.click_login_button_at_admin_panel()

    def search_the_user(self, driver, username):
        s_actions = ScienceActions(driver)
        s_actions.enter_user_for_search(username)
        s_actions.click_search()
