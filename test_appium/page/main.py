from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.profile import Profile
from page.quotes import Quotes
from page.search import Search


class Main(BasePage):
    def goto_search_page(self):
        # self.find(MobileBy.ID, "tv_search").click()
        self.steps("..//page//main.yaml")
        return Search(self._driver)

    def goto_stocks(self):
        pass

    def goto_profile(self):
        self.find(MobileBy.XPATH, "//*[@text='我的']").click()
        return Profile(self._driver)

    def goto_quote(self):
        self.find(MobileBy.XPATH, "//*[@text='行情']").click()
        return Quotes(self._driver)