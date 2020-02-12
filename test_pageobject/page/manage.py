from time import sleep

from selenium.webdriver.common.by import By

from test_pageobject.page.base_page import BasePage


class Manage(BasePage):
    def goto_message(self):
        message_locator = (By.PARTIAL_LINK_TEXT, "消息群发")
        self.find(message_locator).click()

        return self

    def send_message(self, app="", group="", contact=""):
        select_app_locator = (By.PARTIAL_LINK_TEXT, "选择需要发消息的应用")
        app_locator = (By.CSS_SELECTOR, 'div[data-name*="%s"]' % app)
        submit_locator = (By.PARTIAL_LINK_TEXT, "确定")
        select_range_locator = (By.PARTIAL_LINK_TEXT, "选择发送范围")
        search_item_locator = (By.CSS_SELECTOR, "#searchResult li")
        commit_locator = (By.LINK_TEXT, "确认")
        text_locator = (By.CSS_SELECTOR, "textarea.js_send_msg_text")
        send_locator = (By.LINK_TEXT, "发送")

        self.find(select_app_locator).click()
        self.find(app_locator).click()
        self.find(submit_locator).click()
        self.find(select_range_locator).click()
        sleep(3)
        # self.find(search_locator).click()
        search_element = self._driver.find_elements(By.CSS_SELECTOR, "input.ww_searchInput_text")[-1]
        search_element.send_keys(group)
        self.find(search_item_locator).click()
        self.find(commit_locator).click()
        self.find(text_locator).send_keys(contact)
        self.wait_until_click(20, send_locator)
        # self.find(send_locator).click()
        self._driver.execute_script("arguments[0].click();", self.find(send_locator))
        self.find(submit_locator).click()

        return self

    def goto_material_bank(self):
        material_bank_locator = (By.PARTIAL_LINK_TEXT, "素材库")
        self.find(material_bank_locator).click()

        return self

    def goto_add_picture(self):
        add_picture_locator = (By.PARTIAL_LINK_TEXT, "图片")
        self.find(add_picture_locator).click()

        return self

    def add_picture(self, file_path):
        add_picture_locator = (By.PARTIAL_LINK_TEXT, "添加图片")
        upload_locator = (By.ID, "js_upload_input")
        picture_locator = (By.CSS_SELECTOR, ".js_show_image")
        submit_locator = (By.LINK_TEXT, "完成")

        self.find(add_picture_locator).click()
        self.wait_until_presence(20, upload_locator)
        self.find(upload_locator).send_keys(file_path)
        self.wait_until_presence(20, picture_locator)
        self.find(submit_locator).click()

        return self





