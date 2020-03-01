from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Profile(BasePage):
    def login_by_password(self, username, password):
        login_locator = (MobileBy.XPATH, '//*[@text="帐号密码登录"]')
        login_account_locator = (MobileBy.ID, "login_account")
        self.wait_click(20, login_locator)
        self.find(login_locator).click()
        self.wait_click(20,login_account_locator)
        self.find(login_account_locator).send_keys(username)
        self.find(MobileBy.ID, "login_password").send_keys(password)
        self.find(MobileBy.XPATH, '//*[@text="登录" and contains(@resource-id, "button_next")]').click()
        toast = self.find(MobileBy.ID, "md_content").text
        self.find(MobileBy.ID, "md_buttonDefaultPositive").click()
        return toast
