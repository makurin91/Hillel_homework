from HomeWork_9.BaseApp import BasePage
from selenium.webdriver.common.by import By


class MyLocators:
    # Create user / Login page
    username_input = (By.XPATH, '//input[contains(@name,"username")]')
    password_input = (By.XPATH, '//input[contains(@name,"password")]')
    confirm_password_input = (By.XPATH, '//input[contains(@name,"password2")]')
    login_btn = (By.XPATH, '//input[@value="Log in"]')
    dashboard_login_btn = (By.XPATH, '//a[contains(@href,"/api-auth/login/?next=/")]')
    # Site administration
    add_user_btn = (By.XPATH, '//a[contains(@href,"/admin/auth/user/add/")]')
    users_btn = (By.XPATH, '//a[contains(@href,"/admin/auth/user/")]')
    # Creating user page
    save_create_user_btn = (By.XPATH, '//input[contains(@name,"_save")]')
    success_message = (By.XPATH, '//li[@class="success"]')
    # User list
    select_user = (By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/th/a')
    email_field = (By.XPATH, '//td[@class="field-email"]')
    first_name_field = (By.XPATH, '//td[@class="field-first_name"]')
    last_name_field = (By.XPATH, '//td[@class="field-last_name"]')
    search_input = (By.XPATH, '//input[contains(@name,"q")]')
    search_btn = (By.XPATH, '//input[@value="Search"]')
    # User page
    delete_btn = (By.XPATH, '//a[contains(text(), "Delete")]')
    confirm_delete_message = (By.XPATH, '//*[@id="content"]/p')
    yes_delete_btn = (By.XPATH, '//input[@value="Yes, I’m sure"]')
    first_name_input = (By.XPATH, '//input[contains(@name,"first_name")]')
    last_name_input = (By.XPATH, '//input[contains(@name,"last_name")]')
    email_input = (By.XPATH, '//input[contains(@name,"email")]')
    save_update_user = (By.XPATH, '//input[@value="Save"]')
    # User Dashboard
    general_drop_down = (By.XPATH, '//a[@class="dropdown-toggle"]')


class ScienceActions(BasePage):

    def enter_username_for_login(self, username):
        self.type_into(self.find_element(MyLocators.username_input), username)

    def enter_password_for_login(self, password):
        self.type_into(self.find_element(MyLocators.password_input), password)

    def click_login_button_at_admin_panel(self):
        self.click(self.find_element(MyLocators.login_btn))

    def click_login_button_at_user_dashboard(self):
        self.click(self.find_element(MyLocators.dashboard_login_btn))

    def click_add_user_button(self):
        self.click(self.find_element(MyLocators.add_user_btn))

    def enter_username_for_creating_user(self, username):
        self.type_into(self.find_element(MyLocators.username_input), username)

    def enter_password_for_creating_user(self, password):
        self.type_into(self.find_element(MyLocators.password_input), password)

    def enter_confirm_password_for_creating_user(self, password):
        self.type_into(self.find_element(MyLocators.confirm_password_input), password)

    def click_save_creating_user(self):
        self.click(self.find_element(MyLocators.save_create_user_btn))

    def get_text_from_success_message(self):
        element = self.find_element(MyLocators.success_message)
        return element.text

    def get_text_from_dropdown(self):
        element = self.find_element(MyLocators.general_drop_down)
        return element.text

    def click_users_button(self):
        self.click(self.find_element(MyLocators.users_btn))

    def enter_user_for_search(self, username):
        el = self.find_element(MyLocators.search_input)
        self.clear_input(el)
        el.send_keys(username)

    def click_search(self):
        self.click(self.find_element(MyLocators.search_btn))

    def select_first_user_after_search(self):
        self.click(self.find_element(MyLocators.select_user))

    def change_username(self, new_username):
        el = self.find_element(MyLocators.username_input)
        self.clear_input(el)
        el.send_keys(new_username)

    def enter_personal_info(self, first_name, last_name, email):
        self.type_into(self.find_element(MyLocators.first_name_input), first_name)
        self.type_into(self.find_element(MyLocators.last_name_input), last_name)
        self.type_into(self.find_element(MyLocators.email_input), email)

    def click_save_updating_user(self):
        self.click(self.find_element(MyLocators.save_update_user))

    def get_text_email_from_users_list(self):
        el = self.find_element(MyLocators.email_field)
        return el.text

    def get_text_first_name_from_users_list(self):
        el = self.find_element(MyLocators.first_name_field)
        return el.text

    def get_text_last_from_users_list(self):
        el = self.find_element(MyLocators.last_name_field)
        return el.text

    def click_delete_button(self):
        self.click(self.find_element(MyLocators.delete_btn))

    def get_text_confirm_delete_message(self):
        el = self.find_element(MyLocators.confirm_delete_message)
        return el.text

    def click_confirm_delete_button(self):
        self.click(self.find_element(MyLocators.yes_delete_btn))
