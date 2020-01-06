from selenium.webdriver.common.by import By

from test_selenium.page.main_page import BasePage
from test_selenium.page.register import Register


class Login(BasePage):
    _register_bar= (By.CSS_SELECTOR, ".login_registerBar_link")

    def register(self):
        self._driver.find_element(*self._register_bar).click()
        return Register(self._driver)
