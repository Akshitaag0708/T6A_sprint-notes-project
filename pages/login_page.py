from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    LOGIN_LINK = (By.XPATH,"//a[.='Login']")
    EMAIL = (By.ID,"email")
    PASSWORD = (By.ID,"password")
    LOGIN_BTN = (By.XPATH, "//button[.='Login']")

    def login(self , email ,password):

        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK))
            self.click(self.LOGIN_LINK)

        except TimeoutException:
            print("Already on login page")

        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.js_click(self.LOGIN_BTN)