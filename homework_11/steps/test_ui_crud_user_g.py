from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By

scenarios("../features/web_ui_crud_user.feature")


@given(parsers.re("I go to the '(?P<add_user_url>.*)' page"))
def go_to_url(browser, login_ui, add_user_url):
    browser.get(add_user_url)


@given(parsers.re("I enter '(?P<username>.*)' in the username field"))
def enter_username(browser, username):
    username_field = browser.find_element(
        By.XPATH, '//*[@id="id_username"]')
    username_field.click()
    username_field.send_keys(username)


@given(parsers.re("I enter '(?P<password>.*)' in the password field"))
def enter_password(browser, password):
    password_field = browser.find_element(By.XPATH, '//*[@id="id_password1"]')
    password_field.click()
    password_field.send_keys(password)


@given(parsers.re("I enter '(?P<password_confirm>.*)' in the password"
                  " confirmation field"))
def enter_password_confirm(browser, password_confirm):
    confirm_pass_field = browser.find_element(
        By.XPATH, '//*[@id="id_password2"]')
    confirm_pass_field.click()
    confirm_pass_field.send_keys(password_confirm)


@when("I click on the Save button")
def click_save_button(browser):
    save_button = browser.find_element(
        By.XPATH, '//*[@id="user_form"]/div/div/input[1]')
    save_button.submit()


@then(parsers.re("'(?P<change_user>.*)' page is opened"))
def change_user_page(browser, change_user):
    title_page = browser.find_element(By.XPATH, '//*[@id="content"]/h1')
    actual_result = title_page.text
    assert actual_result == change_user


@then(parsers.re("The notification '(?P<notification>.*)'"
                 " is displayed at the top page"))
def notification_success(request, browser, notification):
    notification_success = browser.find_element(
        By.XPATH, '//*[@id="main"]/div/ul/li')
    actual_result = notification_success.text
    assert actual_result == notification


@then(parsers.re("The notification '(?P<notification_success>.*)' is shown"))
def notification_success(browser, notification_success):
    notification = browser.find_element(By.XPATH, '//*[@id="main"]/div/ul/li')
    actual_result = notification.text
    assert actual_result == notification_success


@when(parsers.re("I click '(?P<username>.*)' on the page"))
def find_user(browser, username):
    user_link = browser.find_element(By.LINK_TEXT, username)
    user_link.click()


@then(parsers.re("'(?P<username>.*)' is shown into the Username field"))
def verify_username(browser, username):
    username_field = browser.find_element(By.XPATH, '//*[@id="id_username"]')
    actual_result = username_field.get_attribute('value')
    assert actual_result == username


@given(parsers.re("I click '(?P<username>.*)' on the page"))
def find_user(browser, username):
    user_link = browser.find_element(By.LINK_TEXT, username)
    user_link.click()


@given(parsers.re("Enter '(?P<first_name>.*)' to the first name field"))
def enter_first_name(browser, first_name):
    first_name_field = browser.find_element(
        By.XPATH, '//*[@id="id_first_name"]')
    first_name_field.click()
    first_name_field.send_keys(first_name)


@given(parsers.re("Enter '(?P<last_name>.*)' to the last name field"))
def enter_last_name(browser, last_name):
    last_name_field = browser.find_element(
        By.XPATH, '//*[@id="id_last_name"]')
    last_name_field.click()
    last_name_field.send_keys(last_name)


@given("I click on the Delete button")
def delete_user(browser):
    delete_button = browser.find_element(
        By.XPATH, '//*[@id="user_form"]/div/div/p/a')
    delete_button.click()


@when("I click on the Yes, I'm sure button")
def confirm_deleting(browser):
    confirm_button = browser.find_element(
        By.XPATH, '//*[@id="content"]/form/div/input[2]')
    confirm_button.submit()