import pytest
import time
from pages.search_page import SearchPage
from data.test_data import SEARCH_PRODUCTS
from utilis.test_runner import create_driver
from utilis.assertions import assert_true

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
        self.se_arch_page.enter_search_query(search_product_name)
        self.se_arch_page.click_search_btn()

        search_results_valid=self.se_arch_page.validate_search_query()
        assert_true(search_results_valid,f"the search item{search_product_name}and display does not match:{search_results_valid}")
