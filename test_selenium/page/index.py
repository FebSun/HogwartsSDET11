from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_selenium.page.login import Login
from test_selenium.page.main_page import BasePage
from test_selenium.page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    _register_wx = (By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn")
    _login_btn = (By.CSS_SELECTOR, ".index_top_operation_loginBtn")

    def goto_register(self):
        self._driver.find_element(*self._register_wx).click()
        return Register(self._driver)

    def goto_login(self):
        self._driver.find_element(*self._login_btn).click()
        return Login(self._driver)
