import json
import os
import time
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def docker():
    """
    Running docker container before test start and remove the container after test
    :return:
    """
    os.system("docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm "
              "selenium/standalone-chrome-debug")
    time.sleep(5)
    yield
    os.system("docker rm -f selenium_chrome")


@pytest.fixture
def driver_setup(request):
    """
    Setup driver for tests
    :param request: obj for 'add finalizer'
    :return: driver
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options, )
    driver.implicitly_wait(3)

    def driver_teardown():
        driver.close()

    request.addfinalizer(driver_teardown)
    return driver


@pytest.fixture(scope='class')
def read_data_file(request):
    file = 'data.json'
    with open(file, 'r') as f:
        data = json.load(f)
        USER_URL = data['resources']['user_url']
        ADMIN_URL = data['resources']['admin_url']

        USERS_ENDPOINT = data['api']['user_path']

        USER_NAME = data['simple_user']['username']
        USER_PASSWORD = data['simple_user']['password']
        USER_FIRST_NAME = data['simple_user']['first_name']
        USER_LAST_NAME = data['simple_user']['last_name']
        USER_EMAIL = data['simple_user']['email']
        NEW_USER_NAME = data['simple_user']['new_username']

        ADM_USERNAME = data['admin_user']['username']
        ADM_PASSWORD = data['admin_user']['password']

        request.cls.USER_NAME = USER_NAME
        request.cls.USER_PASSWORD = USER_PASSWORD
        request.cls.USER_FIRST_NAME = USER_FIRST_NAME
        request.cls.USER_LAST_NAME = USER_LAST_NAME
        request.cls.USER_EMAIL = USER_EMAIL
        request.cls.NEW_USER_NAME = NEW_USER_NAME
        request.cls.ADM_USERNAME = ADM_USERNAME
        request.cls.ADM_PASSWORD = ADM_PASSWORD
        request.cls.USER_URL = USER_URL
        request.cls.ADMIN_URL = ADMIN_URL
        request.cls.USERS_ENDPOINT = USERS_ENDPOINT
        yield
