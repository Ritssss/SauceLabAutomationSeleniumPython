from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    SELECT_PRD = (By.XPATH,"//a[@id='product-1']")
    PRODUCT_TITLE = (By.XPATH, "//a[contains(@href,'/products/')]")
    ADD_TO_CART = (By.XPATH,"//input[@value='Add to Cart']")

    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("select product")
    def select_product(self):
        try:
            self.click_element(self.SELECT_PRD)
            return True
        except:
            print("product could not be select")
            return False

    @allure.step("Get selected product name")
    def get_product_name(self):
        product_name = self.get_text(self.PRODUCT_TITLE).strip()
        print("Product selected:", product_name)
        allure.attach(
        product_name,
        name="Selected Product Name",
        attachment_type=allure.attachment_type.TEXT
    )
        return product_name

    @allure.step("Add product to cart")
    def add_to_cart(self):
        try:
            self.click_element(self.ADD_TO_CART)
            return True
        except:
            print("Product couldnot be able to add to cart")
            return False

    def cart_product(self):
        self.select_product()
        self.get_product_name()
        self.add_to_cart()

