import pytest
import time
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from data.test_data import SEARCH_PRODUCTS
from utilis.test_runner import create_driver
from utilis.assertions import assert_true
import allure
from utilis.assertions import assert_true

class TestSearch:
    def setup_method(self):
        self.driver=create_driver()
        self.se_arch_page=SearchPage(self.driver)
        self.ca_rt_page=CartPage(self.driver)
        self.driver.get("https://sauce-demo.myshopify.com/")


    def teardown_method(self):
        self.driver.quit()

    @allure.feature("Shopping Cart")
    @allure.story("User adds product to cart")
    @pytest.mark.parametrize("cart_data", SEARCH_PRODUCTS)
    def test_cart(self, cart_data):
        cart_item=cart_data['product_name']

        with allure.step("search product"):
            self.se_arch_page.search_product(cart_item)
            print(f"search product is:{cart_item}")

        with allure.step("select searched product"):
            self.ca_rt_page.select_product()
            allure.attach(cart_item, name="cart item", attachment_type=allure.attachment_type.TEXT)
            print(f"select searched product: {cart_item}")


        with allure.step("Get searched product name"):
            actual_product_name=self.ca_rt_page.get_product_name()
            print(f"Product page name: {actual_product_name}")

        with allure.step("Assert searched product matches product page title"):
            assert_true(
                cart_item.lower() in actual_product_name.lower(),
                f"Expected '{cart_item}' to be part of '{actual_product_name}'"
            )

        with allure.step("Add searched product to cart"):
            self.ca_rt_page.add_to_cart()
            print("add searched product to cart")


