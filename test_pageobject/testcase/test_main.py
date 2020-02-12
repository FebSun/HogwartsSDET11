from test_pageobject.page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member("1111111", "111", "852", "898989898")
        # assert "aaa" in self.main.import_user().get_message()

    def test_send_message(self):
        message = self.main.send_message()
        message.send_message("十一", "十一", "content")
        # assert "content" in message.get_history()

    def test_import_user(self):
        contact = self.main.import_user().import_user("E:\\file\\通讯录批量导入模板.xlsx")
        # assert "张三" in contact.get_user_message()

    def test_upload_pic(self):
        self.main.goto_manage().goto_material_bank().goto_add_picture().add_picture("E:\\file\\111.png")

    def test_contact_add_member(self):
        self.main.goto_contact().goto_add_member().add_member('testerhome', 'testerhome001', 'testerhome001', '女',
            '852', '98765432', '0523-87654321','testerhome001@testerhome.com', '艾欧尼亚', 2, ("十一", "广州"),
            '测试', '上级', "自定义", "小喽啰", False, "E:\\file\\111.png")

    def test_contact_edit_member(self):
        edit = self.main.goto_contact().goto_edit_member("888888888")
        if edit:
            edit.edit_member('testerhome', 'fafaf', '男', '852',
                '11111111', '0523-87654321', 'testerhome001@testerhome.com', '艾欧尼亚', 2, ("广州", "十一"),
                '测试', '上级', "自定义", "小喽啰", "E:\\file\\111.png")

    def test_contact_delete_member(self):
        self.main.goto_contact().delete_member(0, (1, 2, 3))
        self.main.goto_contact().delete_member(1, ("testerhome", "张三", "11"))
        self.main.goto_contact().delete_member(2, ("888888888", "11", "11"))
        self.main.goto_contact().delete_member(3)


