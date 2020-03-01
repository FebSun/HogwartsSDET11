from page.app import App


class TestProfile:
    def setup(self):
        self.profile = App().start().main().goto_profile()

    def test_login_by_password(self):
        assert "错误" in self.profile.login_by_password("13120837001", "1234556789")