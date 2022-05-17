from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")

    def scroll_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return element

    def click(self, element):
        self.scroll_to_element(element)
        element.click()
        return element

    def clear_input(self, element):
        self.click(element)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        return element

    def type_into(self, element, data):
        self.click(element)
        element.send_keys(data)
        return element

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
