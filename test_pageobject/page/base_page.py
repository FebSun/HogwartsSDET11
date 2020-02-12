from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None, reuse=False, url=None):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if url is None:
            if self._base_url != "":
                self._driver.get(self._base_url)
        else:
            self._driver.get(url)

    def find(self, locator, value=None):
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)

    def type(self, locator, value=None, text=""):
        # text：代表输入的类型
        #     ""：  代表不输入任何内容
        #     " "： 代表清空内容
        #     else：代表输入value值
        if text != "":
            if text == " ":
                self.find(locator, value).clear()
            else:
                self.find(locator, value).clear()
                self.find(locator, value).send_keys(text)

    def wait_until_presence(self, timeout, element):
        WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(element))

    def wait_until_visible(self, timeout, element):
        WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(element))

    def wait_until_click(self, timeout, element):
        WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable(element))

    def close(self):
        self._driver.quit()
