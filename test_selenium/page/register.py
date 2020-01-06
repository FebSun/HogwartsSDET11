from selenium.webdriver.common.by import By

from test_selenium.page.main_page import BasePage


class Register(BasePage):
    _corp_name = (By.ID, "corp_name")
    _submit_btn = (By.ID, "submit_btn")
    _error_msg = (By.CSS_SELECTOR, ".js_error_msg")

    def register_error(self, company):
        self._driver.find_element(*self._corp_name).send_keys(company)
        self._driver.find_element(*self._submit_btn).click()
        return self

    def get_error_msg(self):
        result = []
        for element in self._driver.find_elements(*self._error_msg):
            result.append(element.text)

        return result
