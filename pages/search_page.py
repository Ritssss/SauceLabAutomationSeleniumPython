from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class SearchPage(BasePage):

    SEARCH_INPUT = (By.XPATH,"//input[@id='search-field']")
    SEARCH_BTN=(By.XPATH,"//input[@id='search-submit']")

    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("Search for product: {query}")
    def enter_search_query(self,query):
        self.enter_text(self.SEARCH_INPUT, query)

    @allure.step("click search button")
    def click_search_btn(self):
        try:
            self.click_element(self.SEARCH_BTN)
        except:
            print("search button is not clickable")

    @allure.step("validate search product")
    def validate_search_query(self):
        current_url = self.driver.current_url
        if "search" in current_url:
            return True
        else:
            print("Search page not loaded correctly")
            return False