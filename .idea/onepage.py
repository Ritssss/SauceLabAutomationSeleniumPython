
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #Specifies ChromeDriver path & manages its process
from selenium.webdriver.chrome.options import Options #Options is used to customize the Chrome browser behavior before launching it.
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait #wait import gareko
from selenium.webdriver.support import expected_conditions as EC #yo bhaneko explicit wait

chrome_options=Options()
chrome_options.add_argument("--start-maximized")

#location of chromedrive
service = Service("C:\\Users\\Sriza\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")


#initialize the driver
driver=webdriver.Chrome(service=service, options=chrome_options) #use garna ko lagi bhitra lekheko lekhni

driver.get("https://sauce-demo.myshopify.com/")

wait=WebDriverWait(driver, 10)

def click_element(driver, a):
    element=driver.find_element(By.XPATH, a)
    element.click()

def send_key_to_element(driver, xpath, key):
    element=driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(key)

def clear_element(driver, xpath):
    element=driver.find_element(By.XPATH, xpath)
    element.clear()

'''signup="//a[text()='Sign up']"
click_element(driver, signup)
print("sign link clicked")

#sab page ko assertion garnu parcha hamile sabse easy best way to do this is:
if "register" in driver.current_url:
    print("registered is successful")
else:
    pritnt("warning: registration page may have not loaded properly current url:", driver.current_url)

first_name= "//input[@id='first_name']"
send_key_to_element(driver, first_name, "ritika")

last_name="//input[@id='last_name']"
send_key_to_element(driver, last_name, "stha")

email="//input[@id='email']"
unique_email=f"testUser{int(time.time())}@gmail.com"
send_key_to_element(driver,email, unique_email)

pw="//input[@id='password']"
send_key_to_element(driver,pw,"ritika*88")

btn="//input[@value='Create']"
click_element(driver, btn)

logout_element=driver.find_element(By.XPATH, "//a[text()='Log Out']")
if logout_element:
    print("signup sucessfully, u r now in dashboard")
    
else:
    print("signup page not loaded")'''

#------------------------------------------------------------------------------------
login="//a[text()='Log In']"
click_element(driver,login)
if "register" in driver.current_url:
    print("login is successful")
else:
    print("warning: login page may have not loaded properly current url:", driver.current_url)


email="//input[@id='customer_email']"
send_key_to_element(driver,email, "stharitika0@gmail.com")

pw="//input[@id='customer_password']"
send_key_to_element(driver,pw,"Ritika*88")

btn="//input[@value='Sign In']"
click_element(driver, btn)

'''logout_element=driver.find_element(By.XPATH, "//a[text()='Log Out']")
if logout_element:
    print("signup sucessfully, u r now in dashboard")

else:
    print("signup page not loaded")'''

time.sleep(80)


'''signup=wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign up']"))
).click()

first_name = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='first_name']"))
)
first_name.clear()
first_name.send_keys("ritika")

last_name=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='last_name']"))
).send_keys("shrestha")

email=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))
).send_keys("stharitika0@gmail.com")

pw=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
).send_keys("Ritika*88")

create=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@value='Create']"))
).click()

dashboard=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[text()='Log Out']"))
)

#login
login=wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Log In']"))
).click()

email=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_email']"))
).send_keys("stharitika0@gmail.com")

pw=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_password']"))
).send_keys("Ritika*88")

btn=wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='Sign In']"))
).click()

entry=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[text()='Log Out']"))
)
'''

driver.quit()