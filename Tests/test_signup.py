import pytest
import time
from pages.registration import SignupPage
from data.test_data import SIGNUP_DATA
from utilis.test_runner import create_driver
from utilis.assertions import assert_true
import allure
from utilis.assertions import assert_true

class TestSearch:
    def setup_method(self):
        self.driver=create_driver()
        self.sign_up_page=SignupPage(self.driver)
        self.driver.get("https://sauce-demo.myshopify.com/")


    def teardown_method(self):
        self.driver.quit()

    @allure.feature("User Registration")
    @allure.story("User signs up with valid and invalid details")
    @pytest.mark.parametrize("signup_data", SIGNUP_DATA)
    def test_signup(self, signup_data):

        with allure.step("fill registration form:"):
            self.sign_up_page.click_signup_link()
            self.sign_up_page.enter_first_name(signup_data['first_name'])
            self.sign_up_page.enter_last_name(signup_data['last_name'])
            self.sign_up_page.enter_email(signup_data['email'])
            self.sign_up_page.enter_pw(signup_data['pw'])

        with allure.step("Click create account button"):
            self.sign_up_page.click_signup_btn()
            print("form is filled and signup button is clicked")

        with allure.step("verify registration success"):
            is_registered = self.sign_up_page.verify_registration_success()

            assert_true(is_registered,"Registration failed: Log Out link not visible after signup")
