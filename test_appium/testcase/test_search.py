import pytest
import yaml

from page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page().search("alibaba").get_price("BABA") > 200

    # @pytest.mark.parametrize("key, stock_type, price", [
    #     ("alibaba", "BABA", 205),
    #     ("alibaba", "09988", 205)
    # ])
    @pytest.mark.parametrize("key, stock_type, price", yaml.safe_load(open("data.yaml")))
    def test_search_data(self, key, stock_type, price):
        assert self.main.goto_search_page().search(key).get_price(stock_type) > price
