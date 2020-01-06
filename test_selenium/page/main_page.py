from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.get(self._base_url)
            self._driver.implicitly_wait(5)
            self._driver.maximize_window()
        else:
            self._driver = driver

    def close(self):
        self._driver.quit()
