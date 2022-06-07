import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# docker run -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug


options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--start-maximized')
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options, )

search_input = '//input[@type="search"]'
title_for_check = 'using-the-python-client-driver'


driver.get("https://www.selenium.dev/")
find_search_input = driver.find_element(By.XPATH, search_input)
find_search_input.click()
find_search_input.send_keys('Python documentation')
time.sleep(3)
find_search_input.send_keys(Keys.ENTER)
find_title_for_check = driver.find_element(By.ID, title_for_check)
title_text = find_title_for_check.text
time.sleep(3)
assert title_text == 'Using the Python Client Driver'



