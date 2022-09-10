import os
import time
import pytest
from test_data import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def run_docker():
    os.system("docker run -d -p 4444:4444 -p 5900:5900 --shm-size=2g "
              "--name CRUD_for_user selenium/standalone-chrome-debug")
    time.sleep(4)
    yield
    os.system("docker stop CRUD_for_user")
    os.system("docker rm /CRUD_for_user")


@pytest.fixture()
def browser(run_docker):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors=yes')

    driver = webdriver.Remote(
        command_executor=REMOTE_HOST,
        options=options
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_ui(browser):
    browser.get(BASE_URL)
    input_username = browser.find_element(By.XPATH, '//*[@id="id_username"]')
    input_username.click()
    input_username.send_keys(ADMIN_LOGIN)
    input_pass = browser.find_element(By.XPATH, '//*[@id="id_password"]')
    input_pass.click()
    input_pass.send_keys(f"{ADMIN_PASS}123")
    click_login_btn = browser.find_element(
        By.XPATH, '//*[@id="login-form"]/div[3]/input')
    click_login_btn.submit()







