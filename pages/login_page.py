from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.XPATH,"//a[.='Login']")

    EMAIL = (By.ID,"email")

    PASSWORD = (By.ID,"password")

    LOGIN_BTN = (By.XPATH, "//button[.='Login']")

    def login(self, email, password):

        self.scroll_by_offset()

        self.click(self.LOGIN_LINK)

        self.type(self.EMAIL, email)

        self.type(self.PASSWORD, password)

        self.js_click(self.LOGIN_BTN)