from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts_mumu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # # caps["unicodeKeyboard"] = True
        # # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True
        # caps["chromedriverExecutableDir"] = "E:\\chromedriver"
        caps["chromedriverExecutable"] = "E:\\chromedriver\\2.20\\chromedriver.exe"
        # caps["chromedriverChromeMappingFile"] = "E:\\HogwartsSDET11\\test_appium\\chromeDriverMapping.json"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MobileBy.ID, "tv_agree")))
        agree_elements = self.driver.find_elements(MobileBy.ID, "tv_agree")
        if len(agree_elements) != 0:
            agree_elements[0].click()

    def test_search(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("alibaba")

    def test_search_hk_price(self):
        stock_locator = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]/*[@text='股票']")
        price_locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'current_price')]")

        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*stock_locator).click()
        price = self.driver.find_element(*price_locator).text
        assert float(price) < 218

    def test_check_optional_status(self):
        stock_locator = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]/*[@text='股票']")
        optional_locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'follow_btn')]")
        already_locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id, 'followed_btn')]")
        next_time_locator = (MobileBy.XPATH, "//*[@text='下次再说' and contains(@resource-id, 'tv_left')]")

        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*stock_locator).click()
        self.driver.find_element(*optional_locator).click()
        next_time_element = self.driver.find_elements(*next_time_locator)
        if len(next_time_element) != 0:
            next_time_element[0].click()

        self.driver.find_element(MobileBy.ID, "action_close").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*stock_locator).click()
        optional_status = self.driver.find_element(*already_locator).get_attribute("text")
        print(optional_status)
        assert "已添加" == optional_status

    def test_scroll(self):
        # scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
        #                      'new UiScrollable('
        #                      'new UiSelector().className("androidx.viewpager.widget.ViewPager"))'
        #                      '.scrollIntoView(new UiSelector().text("3小时前"));')

        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable('
                             'new UiSelector().scrollable(true).instance(0)).'
                             'scrollIntoView(new UiSelector().text("3小时前"));')

        self.driver.find_element(*scroll_to_element)

    def test_selector(self):
        selector_element = (MobileBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("飞翔的小乌龟");')
        self.driver.find_element(*selector_element).click()

    def test_touch(self):
        size = self.driver.get_window_size()
        element = self.driver.find_element(MobileBy.ID, "status_single_image")
        action = TouchAction(self.driver)
        action.long_press(x=size['width'] * 0.5, y=size['height'] * 0.8).\
            move_to(x=size['width'] * 0.2, y=size['height'] * 0.0).\
            release().perform()

    def test_webview_natvie(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        edit_element = self.driver.find_elements(MobileBy.XPATH, "//*[@class='android.widget.EditText']")
        edit_element[0].send_keys("13120837001")

    def test_webview_debug(self):
        phone_locator = (By.ID, "phone-number")
        trade_locator = (By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]")

        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(trade_locator))
        self.driver.find_element(*trade_locator).click()
        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(0.5)
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.contexts) > 1)
        # print(self.driver.page_source)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.page_source)
        # print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI h1").click()
        # print(self.driver.window_handles)
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(phone_locator))
        self.driver.find_element(*phone_locator).send_keys("13120837001")

    def test_nasdaq_open_account(self):
        trade_locator = (By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]")
        open_account_locator = (By.CSS_SELECTOR, ".trade_home_xueying_SJY .trade_home_info_3aI h1")
        phone_locator = (By.CSS_SELECTOR, "input[placeholder='请输入手机号']")
        verify_code_locator = (By.CSS_SELECTOR, "input[placeholder='请输入验证码']")
        toast_locator = (By.CSS_SELECTOR, ".Toast_toast_22U span")
        submit_locator = (By.CSS_SELECTOR, ".open_form-submit_1Ms")
        close_loactor = (MobileBy.ID, "action_bar_close")
        back_loactor = (MobileBy.ID, "action_bar_back")

        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(trade_locator))
        self.driver.find_element(*trade_locator).click()
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(*open_account_locator).click()
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(phone_locator))
        self.driver.find_element(*phone_locator).send_keys("13120837777")
        self.driver.find_element(*verify_code_locator).send_keys("1234")
        self.driver.hide_keyboard()
        self.driver.find_element(*submit_locator).click()
        toast = self.driver.find_element(*toast_locator).text
        assert "请输入正确的验证码！" in toast
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.context(self.driver.contexts[0])
        # 有时候，关闭的按钮无法点击，就换成后退按钮
        # WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(close_loactor))
        # self.driver.find_element(*close_loactor).click()
        self.driver.find_element(*back_loactor).click()

    def teardown(self):
        sleep(10)
        self.driver.quit()
