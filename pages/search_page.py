from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):

    SEARCH_INPUT = (By.XPATH,"//input[@id='search-field']")
    SEARCH_BTN=(By.XPATH,"//input[@id='search-submit']")

    def __init__(self,driver):
        super().__init__(driver)

    def enter_search_query(self,query):
        self.enter_text(self.SEARCH_INPUT, query)

    def click_search_btn(self):
        self.click_element(self.SEARCH_BTN)

    def validate_search_query(self):
        current_url = self.driver.current_url
        if "search" in current_url:
            print("Search page loaded")
            return True
        else:
            print("Search page not loaded correctly")
            return False