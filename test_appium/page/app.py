from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _app_package = "com.xueqiu.android"
    _app_activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "Hogwarts11_6"
            caps["appPackage"] = self._app_package
            caps["appActivity"] = self._app_activity
            # caps["noReset"] = True
            # caps["dontStopAppOnReset"] = True
            # # caps["unicodeKeyboard"] = True
            # # caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True
            # caps["chromedriverExecutableDir"] = "E:\\chromedriver"
            caps["chromedriverExecutable"] = "E:\\chromedriver\\2.20\\chromedriver.exe"
            # caps["chromedriverChromeMappingFile"] = "E:\\HogwartsSDET11\\test_appium\\chromeDriverMapping.json"
            caps["newCommandTimeout"] = 120

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(self._app_package, self._app_activity)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self._driver)
