from time import sleep

from selenium.webdriver.common.by import By

from test_pageobject.page.base_page import BasePage


class Contact(BasePage):
    _head_pic_locator = (By.ID, "js_upload_file")
    _input_locator = (By.CSS_SELECTOR, ".js_file")
    _reload_locator = (By.PARTIAL_LINK_TEXT, "重新上传")
    _pic_save_locator = (By.CSS_SELECTOR, "div.ww_dialog_foot a.js_save")
    _username_locator = (By.NAME, "username")
    _english_name_locator = (By.ID, 'memberAdd_english_name')
    _acct_id_locator = (By.NAME, "acctid")
    _gender_locator = (By.CSS_SELECTOR, 'input[name="gender"]')
    _zip_code_element = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input')
    _mobile_locator = (By.NAME, "mobile")
    _telephone_locator = (By.ID, 'memberAdd_telephone')
    _mail_locator = (By.ID, 'memberAdd_mail')
    _corp_address_locator = (By.ID, 'memberEdit_address')
    _depart_change_locator = (By.LINK_TEXT, "修改")
    _search_locator = (By.CSS_SELECTOR, "input.ww_searchInput_text")
    _item_delete_locator = (By.CSS_SELECTOR, "body>div:nth-last-child(2) span.js_delete")
    _group_locator = (By.CSS_SELECTOR, "#searchResult li")
    _submit_locator = (By.LINK_TEXT, "确认")
    _position_locator = (By.ID, 'memberAdd_title')
    _identity_stat_locator = (By.CSS_SELECTOR, 'input[name="identity_stat"]')
    _external_position_set_locator = (By.CSS_SELECTOR, 'input[name="extern_position_set"]')
    _external_position_locator = (By.CSS_SELECTOR, 'input[name="extern_position"]')
    _send_invite_locator = (By.CSS_SELECTOR, 'input[name="sendInvite"]')
    _save_locator = (By.LINK_TEXT, "保存")

    def goto_add_member(self):
        add_member_locator = (By.LINK_TEXT, "添加成员")
        self.find(add_member_locator).click()
        return self

    def add_member(self, username, english_name, acctId, gender, zipCode, mobile, telephone, mail,
                   corp_address, depart_type, department, position, identity_stat, external_position_set,
                   external_position, sendInvite, pic_path):
        zip_code_locator = (By.CSS_SELECTOR, 'li[data-value="%s"]' % zipCode)

        self.find(self._head_pic_locator).click()
        self.find(self._input_locator).send_keys(pic_path)
        self.wait_until_visible(20, self._reload_locator)
        self.find(self._pic_save_locator).click()
        # self._driver.execute_script("arguments[0].click();", self.find(self._save_locator))
        self.find(self._username_locator).send_keys(username)
        self.find(self._english_name_locator).send_keys(english_name)
        self.find(self._acct_id_locator).send_keys(acctId)
        if gender == "男":
            self._driver.find_elements(*self._gender_locator)[0].click()
        else:
            self._driver.find_elements(*self._gender_locator)[1].click()
        self.find(self._zip_code_element).click()
        self.find(zip_code_locator).click()
        self.find(self._mobile_locator).send_keys(mobile)
        self.find(self._telephone_locator).send_keys(telephone)
        self.find(self._mail_locator).send_keys(mail)
        self.find(self._corp_address_locator).send_keys(corp_address)

        # depart_type: 代表操作类型
        #     0：不做任何改动
        #     1：直接增加
        #     2：删除后，添加
        if depart_type == 1 or depart_type == 2:
            self.find(self._depart_change_locator).click()
            # 先判断是否删除
            if depart_type == 2:
                item_delete_element = self._driver.find_elements(*self._item_delete_locator)
                for element in item_delete_element:
                    element.click()

            search_element = self._driver.find_elements(*self._search_locator)[-1]
            if isinstance(department, tuple):
                for value in department:
                    search_element.send_keys(value)
                    self.find(self._group_locator).click()
            else:
                search_element.send_keys(department)
                self.find(self._group_locator).click()
            self.find(self._submit_locator).click()

        self.find(self._position_locator).send_keys(position)
        if identity_stat == "普通成员":
            self._driver.find_elements(*self._identity_stat_locator)[0].click()
        else:
            self._driver.find_elements(*self._identity_stat_locator)[1].click()
        if external_position_set in "同步公司内职务":
            self._driver.find_elements(*self._external_position_set_locator)[0].click()
        else:
            self._driver.find_elements(*self._external_position_set_locator)[1].click()
            self._driver.find_element(*self._external_position_locator).send_keys(external_position)
        b_selected = self.find(self._send_invite_locator).is_selected()
        if b_selected != sendInvite:
            self.find(self._send_invite_locator).click()
        self.find(self._save_locator).click()

        return self

    def goto_import_user(self):
        import_output_locator = (By.PARTIAL_LINK_TEXT, "批量导入/导出")
        import_locator = (By.PARTIAL_LINK_TEXT, "文件导入")

        self.find(import_output_locator).click()
        self.find(import_locator).click()

        return self

    def import_user(self, file_path=""):
        upload_file_locator = (By.ID, "js_upload_file_input")
        submit_locator = (By.ID, "submit_csv")
        contact_locator = (By.ID, "reloadContact")

        self.find(upload_file_locator).send_keys(file_path)
        self.find(submit_locator).click()
        self.wait_until_visible(20, contact_locator)
        self.find(contact_locator).click()

        return self

    def goto_edit_member(self, tel=""):
        menu_locator = (By.CSS_SELECTOR, 'td[title="%s"]~td.member_colRight_memberTable_td_Status' % tel)
        edit_locator = (By.LINK_TEXT, "编辑")

        element = self._driver.find_elements(*menu_locator)
        if len(element) == 0:
            return None
        else:
            self.find(menu_locator).click()
        self.find(edit_locator).click()

        return self

    def edit_member(self, username, english_name, gender, zipCode, mobile, telephone, mail, corp_address,
                    depart_type, department, position, identity_stat, external_position_set,
                    external_position, pic_path):
        english_name_locator = (By.ID, 'memberEdit_english_name')
        zip_code_locator = (By.CSS_SELECTOR, 'li[data-value="%s"]' % zipCode)
        telephone_locator = (By.ID, "memberEdit_telephone")
        mail_locator = (By.ID, 'memberEdit_mail')
        corp_address_locator = (By.ID, 'memberEdit_address')
        item_delete_locator = (By.CSS_SELECTOR, "span.js_delete")
        position_locator = (By.ID, 'memberEdit_title')

        if pic_path != "":
            self.find(self._head_pic_locator).click()
            self.find(self._input_locator).send_keys(pic_path)
            self.wait_until_visible(20, self._reload_locator)
            self.find(self._pic_save_locator).click()
            # self._driver.execute_script("arguments[0].click();", self.find(self._save_locator))

        self.type(self._username_locator, text=username)
        self.type(english_name_locator, text=english_name)

        if gender == "男":
            self._driver.find_elements(*self._gender_locator)[0].click()
        else:
            self._driver.find_elements(*self._gender_locator)[1].click()
        self.find(self._zip_code_element).click()
        self.find(zip_code_locator).click()
        self.type(self._mobile_locator, text=mobile)
        self.type(telephone_locator, text=telephone)
        self.type(mail_locator, text=mail)
        self.type(corp_address_locator, text=corp_address)

        # depart_type: 代表操作类型
        #     0：不做任何改动
        #     1：直接增加
        #     2：删除后，添加
        if depart_type == 1 or depart_type == 2:
            self.find(self._depart_change_locator).click()
            # 先判断是否删除
            if depart_type == 2:
                item_delete_element = self._driver.find_elements(*self._item_delete_locator)[::-1]
                for element in item_delete_element:
                    element.click()

            search_element = self._driver.find_elements(*self._search_locator)[-1]
            if isinstance(department, tuple):
                for value in department:
                    search_element.send_keys(value)
                    self.find(self._group_locator).click()
            else:
                search_element.send_keys(department)
                self.find(self._group_locator).click()
            self.find(self._submit_locator).click()

        self.type(position_locator, text=position)
        if identity_stat == "普通成员":
            self._driver.find_elements(*self._identity_stat_locator)[0].click()
        else:
            self._driver.find_elements(*self._identity_stat_locator)[1].click()
        if external_position_set in "同步公司内职务":
            self._driver.find_elements(*self._external_position_set_locator)[0].click()
        else:
            self._driver.find_elements(*self._external_position_set_locator)[1].click()
            self._driver.find_element(*self._external_position_locator).send_keys(external_position)
        self.find(self._save_locator).click()

        return self

    def delete_member(self, delete_type, value):
        delete_locator = (By.LINK_TEXT, "删除")

        # delete_type：代表删除的方式
        #     0：代表按序号进行删除
        #     1：代表按姓名查找，将查找到的用户进行删除
        #     2：代表按电话查找，将查找到的用户进行删除
        #     3：代表全部删除
        member_element = self._driver.find_elements(By.CSS_SELECTOR, "td input.ww_checkbox")
        if len(member_element) == 0:
            return None
        else:
            if delete_type == 0:
                if isinstance(value, tuple):
                    for item in value:
                        member_element[item-1].click()
                else:
                    member_element[value-1].click()
            elif delete_type == 1:
                if isinstance(value, tuple):
                    for item in value:
                        name_locator = (By.XPATH, '//td[@title="%s"]/preceding-sibling::td[1]' % item)
                        print(name_locator)
                        member_element = self._driver.find_elements(*name_locator)
                        if len(member_element) != 0:
                            for element in member_element:
                                element.click()
                else:
                    name_locator = (By.XPATH, '//td[@title="%s"]/preceding-sibling::td[1]' % value)
                    member_element = self._driver.find_elements(*name_locator)
                    if len(member_element) != 0:
                        for element in member_element:
                            element.click()
            elif delete_type == 2:
                if isinstance(value, tuple):
                    for item in value:
                        name_locator = (By.XPATH, '//td[@title="%s"]/preceding-sibling::td[4]' % item)
                        print(name_locator)
                        member_element = self._driver.find_elements(*name_locator)
                        if len(member_element) != 0:
                            member_element[0].click()
                else:
                    name_locator = (By.XPATH, '//td[@title="%s"]/preceding-sibling::td[4]' % value)
                    member_element = self._driver.find_elements(*name_locator)
                    if len(member_element) != 0:
                        member_element[0].click()
            else:
                all_locator = (By.CSS_SELECTOR, "th input.ww_checkbox")
                self.find(all_locator).click()

        self.find(delete_locator).click()
