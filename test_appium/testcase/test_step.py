from page.app import App


class TestStep:
    def test_step(self):
        App().start().main().steps("..//page//main.yaml")

    def test_search(self):
        App().start().main().goto_search_page().search("JD")