from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    CHECKOUT_LINK = (By.XPATH,"//a[@class='checkout']")
    CHECKOUT_BTN=(By.XPATH,"//input[@value='Check Out' and @id='checkout']")

    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("click on checkout link")
    def click_checkout_link(self):
        try:
            self.click_element(self.CHECKOUT_LINK)
        except:
            print("checkout link is not visible or not clickable")

    @allure.step("Get checkout item")
    def checkout_item(self,product_name):
        dynamic_locator = (By.XPATH, f"//a[contains(normalize-space(),'{product_name}')]")
        try:
            checkout_product=self.get_text(dynamic_locator).strip()
            print("Checkout product:", checkout_product)
            allure.attach(
                checkout_product,
                name="Checkout Product Name",
                attachment_type=allure.attachment_type.TEXT
            )
            return checkout_product
        except Exception as e:
            print("Checkout product not found:", e)
            return None

    @allure.step("click checkout button")
    def checkout_btn(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CHECKOUT_BTN)
            )

            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)


            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CHECKOUT_BTN)
            )

            # Click using ActionChains (avoids overlays / sticky headers)
            ActionChains(self.driver).move_to_element(button).click().perform()

            print("Successfully clicked checkout button")
            return True

        except Exception as e:
            print("Checkout button is not clickable:", e)
            return False

