import pytest
import time
from pages.login_page import LoginPage
from data.test_data import SIGNUP_DATA
from utilis.test_runner import create_driver
from utilis.assertions import assert_true
import allure
from utilis.assertions import assert_true

class TestSearch:
    def setup_method(self):
        self.driver=create_driver()
        self.log_in_page=LoginPage(self.driver)
        self.driver.get("https://sauce-demo.myshopify.com/")


    def teardown_method(self):
        self.driver.quit()

    @allure.feature("User Authentication")
    @allure.story("User logs in with credentials")
    @pytest.mark.parametrize("login_data", SIGNUP_DATA)
    def test_login(self, login_data):

        with allure.step("fill login form:"):
            self.log_in_page.click_login_link()
            self.log_in_page.enter_email(login_data['email'])
            self.log_in_page.enter_pw(login_data['pw'])

        with allure.step("Click create account button"):
            self.log_in_page.click_login_btn()
            print("form is filled and login button is clicked")

        with allure.step("verify registration success"):
            is_logged_in = self.log_in_page.verify_login_success()

            assert_true(is_logged_in,"login failed: Log Out link not visible after login")
