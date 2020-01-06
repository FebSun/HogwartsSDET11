from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(5)

    def test_register(self):
        self.index = Index(self.driver)
        self.index.goto_register().register_error("采菇凉的小蘑菇")

    def teardown(self):
        sleep(10)
        self.driver.quit()





