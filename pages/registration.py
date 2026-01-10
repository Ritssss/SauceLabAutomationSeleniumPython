
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class SignupPage(BasePage):
    SIGNUP_LINK=(By.XPATH,"//a[text()='Sign up']")
    FIRST_NAME=(By.XPATH,"//input[@id='first_name']")
    LAST_NAME=(By.XPATH,"//input[@id='last_name']")
    EMAIL=(By.XPATH,"//input[@id='email']")
    PW=(By.XPATH,"//input[@id='password']")
    SIGNUP_BTN=(By.XPATH,"//input[@value='Create']")
    LOGOUT_LINK=(By.XPATH, "//a[text()='Log Out']")

    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("click on signup link")
    def click_signup_link(self):
     self.click_element(self.SIGNUP_LINK)

    def enter_first_name(self,first_name):
        try:
            self.enter_text(self.FIRST_NAME, first_name)
            print(f"first name is:{first_name}")
        except:
            print("unable to enter first name")
            return False

    def enter_last_name(self,last_name):
        try:
            self.enter_text(self.LAST_NAME, last_name)
            print(f"last name is:{last_name}")
        except:
            print("unable to enter last name")
            return False

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

    @allure.step("Click create account button")
    def click_signup_btn(self):
        try:
            self.click_element(self.SIGNUP_BTN)
        except:
            print("Signup button is not clickable")


    @allure.step("Verify registration success")
    def verify_registration_success(self):
        try:
            logout_element=self.find_element(self.LOGOUT_LINK)
            if logout_element:
                print("Registration successful - Log Out element found")
                return True
        except:
            print("Registration is not successful - No redirect and Log Out element not found")
            return False
