from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_element(self,locator):
        element=self.find_element(locator)
        element.click()

    def enter_text(self, locator, key):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(key)

    def get_text(self,locator): #yo text return garnu lai
        element = self.find_element(locator)
        return element.text.strip()

    def find_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

