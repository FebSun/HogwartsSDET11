from selenium.webdriver.common.by import By

from test_selenium.page.register import Register


class Index:
    def __init__(self, driver):
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)
