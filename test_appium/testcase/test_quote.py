from page.app import App


class TestQuote:
    def setup(self):
        self.quote = App().start().main().goto_quote()

    def test_search_and_back(self):
        self.quote.search("JD").add_select().back()