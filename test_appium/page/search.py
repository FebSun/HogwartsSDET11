from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.quote import Quote


class Search(BasePage):
    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(MobileBy.ID, "name").click()
        return self

    def get_price(self, key: str = None) -> float:
        stock_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "title_container")]/*[@text="股票"]')
        price_locator = (MobileBy.XPATH, '//*[@text="%s"]/../../..//*[contains(@resource-id, "current_price")]' % key)
        self.wait_click(20, stock_locator)
        self.find(stock_locator).click()
        return float(self.find(price_locator).text)

    def add_select(self):
        self.find(MobileBy.XPATH, '//*[@text="加自选"]').click()
        return self

    def go_back_to_quote(self):
        self.find(MobileBy.XPATH, '//*[@text="取消"]').click()
        return Quote(self)
