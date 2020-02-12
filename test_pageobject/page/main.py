from time import sleep

from selenium.webdriver.common.by import By

from test_pageobject.page.base_page import BasePage
from test_pageobject.page.contact import Contact
from test_pageobject.page.manage import Manage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def add_member(self):
        add_member_locator = (By.PARTIAL_LINK_TEXT, "添加成员")
        # self.find(add_member_locator).click
        self._driver.execute_script("arguments[0].click();", self.find(add_member_locator))

        return Contact(reuse=True)

    def import_user(self):
        import_locator = (By.LINK_TEXT, "导入通讯录")
        self._driver.execute_script("arguments[0].click();", self.find(import_locator))

        return Contact(reuse=True)

    def send_message(self):
        send_message_locator = (By.PARTIAL_LINK_TEXT, "消息群发")
        self._driver.execute_script("arguments[0].click();", self.find(send_message_locator))

        return Manage(reuse=True)

    def goto_manage(self):
        manage_locator = (By.ID, "menu_manageTools")
        self.find(manage_locator).click()

        return Manage(reuse=True)

    def goto_contact(self):
        contact_locator = (By.ID, "menu_contacts")
        self.find(contact_locator).click()

        return Contact(reuse=True)