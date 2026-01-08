
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #Specifies ChromeDriver path & manages its process
from selenium.webdriver.chrome.options import Options #Options is used to customize the Chrome browser behavior before launching it.
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait #wait import gareko
 #yo bhaneko explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options=Options()
chrome_options.add_argument("--start-maximized")

#location of chromedrive
service = Service("C:\\Users\\Sriza\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")


#initialize the driver
driver=webdriver.Chrome(service=service, options=chrome_options) #use garna ko lagi bhitra lekheko lekhni


wait=WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/drag_and_drop")


source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

time.sleep(3)
driver.quit()

