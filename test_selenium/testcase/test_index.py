from time import sleep

from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register_error("采菇凉的小蘑菇")

    def test_login_register(self):
        error_msg = self.index.goto_login().register().register_error("haha").get_error_msg()
        str_error_msg = "|".join(error_msg)
        print(str_error_msg)
        assert "请选择" in str_error_msg

    def teardown(self):
        sleep(10)
        self.index.close()





