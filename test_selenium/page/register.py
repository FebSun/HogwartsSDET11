from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver):
        self.driver = driver

    def register_error(self, company):
        self.driver.find_element(By.ID, "corp_name").send_keys(company)
        self.driver.find_element(By.ID, "submit_btn").click()
        return self
