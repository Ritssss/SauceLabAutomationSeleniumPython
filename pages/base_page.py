from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Assert element exists with xpath: {locator}")
    def find_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("click on element with xpath: {locator}")
    def click_element(self,locator):
        element=self.find_element(locator)
        assert element.is_displayed(), f" element with {locator} is not clickable"
        element.click()
        print(f"succesfully clicked on element:{locator}")

    @allure.step("send keys {key} to the element with xpath {locator}")
    def enter_text(self, locator, key):
        element=self.find_element(locator)
        assert element.is_enabled(), f"key {key} is not enabled in the locator {locator}"
        element.clear()
        element.send_keys(key)
        print(f"successfully send keys {key} to element {locator}")

    @allure.step("get element text in return {locator}")
    def get_text(self,locator): #yo text return garnu lai
        element = self.find_element(locator)
        assert element.is_displayed(), f"element is not displayed {locator}"
        return element.text.strip()

    @allure.step("Assert clickable element exists with xpath: {locator}")
    def find_clickable_element(self,locator):
        try:
            element= self.wait.until(EC.element_to_be_clickable(locator))
            assert element.is_displayed(),f"Element with xpath '{locator}' is not visible"
            print(f"Assertion passed: Element '{locator}' is clickable and visible")
            return True
        except :
            print(f"Assertion failed: Element '{locator}' is not clickable (timeout)")
            return False


    @allure.step("Assert element exists with xpath: {locator}")
    def assert_element_exists(self,locator): #yo bhaneko find_visible element ho
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            element=self.driver.find_element(By.XPATH,locator)
            assert element.is_enabled(), f"element with xpath{locator} is not visible"
            print(f"assertion passed:Element {locator} exists and is visible")
            return True
        except:
            print(f"Assertion failed: Element {locator} does not exists and is not visible")
            return False