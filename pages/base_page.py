from logging import exception

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Assert element exists with xpath: {locator}")
    def find_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("click on element with xpath: {locator}")
    def click_element(self,locator):
        try:
            element=self.find_element(locator)
            assert element.is_displayed(), f" element with {locator} is not clickable"
            element.click()
            print(f"succesfully clicked on element:{locator}")
        except Exception as e:
            element_name=locator.split('/')[-1].replace('"',"").replace("'","")
            self.take_screenshot(f"click failure-{element_name}")
            raise e

    @allure.step("send keys {key} to the element with xpath {locator}")
    def enter_text(self, locator, key):
        try:
            element=self.find_element(locator)
            assert element.is_enabled(), f"key {key} is not enabled in the locator {locator}"
            element.clear()
            element.send_keys(key)
            print(f"successfully send keys {key} to element {locator}")
        except exception as e:
            element_name=locator.split('/')[-1].replace('"',"").replace("'","")
            self.take_screenshot(f"click failure-{element_name}")
            raise e

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
        except exception as e:
            element_name=locator.split('/')[-1].replace('"',"").replace("'","")
            self.take_screenshot(f"click failure-{element_name}")
            print(f"Assertion failed: Element '{locator}' is not clickable (timeout)")
            raise e


    @allure.step("Assert element exists with xpath: {locator}")
    def assert_element_exists(self,locator): #yo bhaneko find_visible element ho
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            element=self.driver.find_element(By.XPATH,locator)
            assert element.is_enabled(), f"element with xpath{locator} is not visible"
            print(f"assertion passed:Element {locator} exists and is visible")
            return True
        except exception as e:
            element_name=locator.split('/')[-1].replace('"',"").replace("'","")
            self.take_screenshot(f"click failure-{element_name}")
            print(f"Assertion failed: Element {locator} does not exists and is not visible")
            return e


    @allure.step("Take screenshot: {name}")
    def take_screenshot(self, name="screenshot", timestamp=True):
        #ss rakhna ko lagi fiest ma hamile euta screenshot bahne directory banaunu parca
        screenshots_dir="screenshots"
        if not os.path.exists(screenshots_dir): #ss dir cha bhane ss katai ni haldaina ss mostly failed case ko huncha
            os.makedirs(screenshots_dir)

        import time
        if timestamp:
            timestamp_str=int(time.time()) #str lai int ma convert gareko
            filename=f"{screenshots_dir}/{name}_{timestamp_str}.png"
        else:
            filename=f"{screenshots_dir}/{name}.png"
        self.driver.save_screenshot(filename)

        allure.attach.file(filename,name=name, attachment_type=allure.attachment_type.PNG)
        print(f"Screenshot taken: {filename}")

