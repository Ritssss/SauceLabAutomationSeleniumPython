import pytest
import time
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from data.test_data import SEARCH_PRODUCTS
from pages.chech_out_page import CheckoutPage
from utilis.test_runner import create_driver
from utilis.assertions import assert_true
import allure
from utilis.assertions import assert_true

class TestSearch:
    def setup_method(self):
        self.driver=create_driver()
        self.se_arch_page=SearchPage(self.driver)
        self.ca_rt_page=CartPage(self.driver)
        self.check_out_page=CheckoutPage(self.driver)
        self.driver.get("https://sauce-demo.myshopify.com/")


    def teardown_method(self):
        self.driver.quit()

    @allure.feature("Checkout")
    @allure.story("User completes checkout with one product")
    @pytest.mark.parametrize("checkout_data", SEARCH_PRODUCTS)
    def test_cart(self, checkout_data):
        checkout_item=checkout_data['product_name']

        with allure.step("search product and add to cart"):
            self.se_arch_page.search_product(checkout_item)
            self.ca_rt_page.cart_product()
            print(f"search product and add to cart product is:{checkout_item}")

        with allure.step("click on checkout link"):
            self.check_out_page.click_checkout_link()
            print("checkout link clicked")

        with allure.step("get checkout item"):
            actual_checkout_item=self.check_out_page.checkout_item(checkout_item)
            print(f"actual checkout item is:{actual_checkout_item}")

        with allure.step("Assert checkout product matches searched product"):
            assert_true(
                checkout_item.lower() in actual_checkout_item.lower(),
                f"Expected '{checkout_item}' to be part of '{actual_checkout_item}'"
            )

        with allure.step("click on checkout button"):
            self.check_out_page.checkout_btn()
            print("successfully checkout product")