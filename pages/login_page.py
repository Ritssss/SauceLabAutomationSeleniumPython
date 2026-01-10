
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    LOGIN_LINK=(By.XPATH,"//a[text()='Log In']")
    EMAIL=(By.XPATH,"//input[@id='customer_email']")
    PW=(By.XPATH,"//input[@id='customer_password']")
    LOGIN_BTN=(By.XPATH,"//input[@value='Sign In']")
    LOGOUT_LINK=(By.XPATH, "//a[text()='Log Out']")

    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("click on signup link")
    def click_login_link(self):
         self.click_element(self.LOGIN_LINK)

    def enter_email(self,email):
        try:
            self.enter_text(self.EMAIL, email)
            print(f"email address is:{email}")
        except:
            print("unable to enter email adddress")
            return False

    def enter_pw(self,password):
        try:
            self.enter_text(self.PW, password)
            print(f"password is:{password}")
        except:
            print("unable to enter password")
            return False

    @allure.step("Click login button")
    def click_login_btn(self):
        try:
            self.click_element(self.LOGIN_BTN)
        except:
            print("Signup button is not clickable")


    @allure.step("Verify login success")
    def verify_login_success(self):
        try:
            logout_element=self.find_element(self.LOGOUT_LINK)
            if logout_element:
                print("Registration successful - Log Out element found")
                return True
        except:
            print("Registration is not successful - No redirect and Log Out element not found")
            return False
