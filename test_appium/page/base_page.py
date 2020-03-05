import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _black_list = [
        (MobileBy.ID, "tv_agree"),
        (MobileBy.ID, "image_cancel"),
        (MobileBy.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 10
    _error_count = 0
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value=None):
        logging.info(locator)
        logging.info(value)
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else \
                self._driver.find_element(locator, value)
            self._error_count = 0
            return element
        except Exception as ex:
            if self._error_count > self._error_max:
                raise ex
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self.finds(element)
                if len(elements) > 0:
                    elements[0].click()
            return self.find(locator, value)

    def finds(self, locator, value: str = None):
        if isinstance(locator, tuple):
            return self._driver.find_elements(*locator)
        else:
            return self._driver.find_elements(locator, value)

    def wait_click(self, timeout=10, locator=None):
        WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_presence(self, timeout=10, locator=None):
        WebDriverWait(self._driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait_visibility(self, timeout=10, locator=None):
        WebDriverWait(self._driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element: WebElement = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute()
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            contents = content.replace("{%s}" % key, self._params["key"])
                        element.send_keys(contents)
