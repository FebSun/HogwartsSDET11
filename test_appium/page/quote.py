from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.search import Search


class Quote(BasePage):
    def search(self):
        self.find(MobileBy.ID, "action_search").click()
        return Search(self._driver)