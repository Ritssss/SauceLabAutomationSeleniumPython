import pytest
import time
from pages.search_page import SearchPage
from data.test_data import SEARCH_PRODUCTS
from utilis.test_runner import create_driver
from utilis.assertions import assert_true
import allure

class TestSearch:
    def setup_method(self):
        self.driver=create_driver()
        self.se_arch_page=SearchPage(self.driver)
        self.driver.get("https://sauce-demo.myshopify.com/")


    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("search_data", SEARCH_PRODUCTS)
    def test_search(self, search_data):
        search_product_name=search_data["product_name"]

        with allure.step(f"Enter search query: {search_product_name}"):
            self.se_arch_page.enter_search_query(search_product_name)
            allure.attach(search_product_name, name="searched product", attachment_type=allure.attachment_type.TEXT)
            print(f"searched product is: {search_product_name}")

        with allure.step("Click on search button"):
            self.se_arch_page.click_search_btn()
            print("search button is clicked")

        with allure.step("validate search result"):
            search_results_valid=self.se_arch_page.validate_search_query()
            if search_results_valid:
                allure.attach("searched result match", "name=validation", attachment_type=allure.attachment_type.TEXT)
                print("search product  and shown product is same")

            else:
                allure.attach("Search result doesnot match", "name=validation", attachment_type=allure.attachment_type.TEXT)
                print("search product and shows product doesnot match")

            assert_true(search_results_valid,f"the search item{search_product_name}and display does not match:{search_results_valid}")
