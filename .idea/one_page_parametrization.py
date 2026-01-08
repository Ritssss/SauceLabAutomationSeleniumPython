
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

wait=WebDriverWait(driver, 10)

def click_element(driver, a):
    element=driver.find_element(By.XPATH, a)
    element.click()

def send_key_to_element(driver, xpath, key):
    element=driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(key)

login_search_data=[
    {
        "email":"stharitika0@gmail.com",
        "pw":"Ritika*11",
        #"search_term":"product"
    },
    {
        "email":"testuser2@gmail.com",
        "pw":"abcde*11",
        #"search_term":"jacket"
    },
    {
        "email":"testuser3@gmail.com",
        "pw":"dertf*88",
        #"search_term":"hat"
    }
]


#yeta aba hamile for loop gareko for test data yesma emurate le data ra index duitai dincha
'''for i, user_data in enumerate(login_search_data):
    #print(f"Running test {i+1} with email: {user_data['email']} and with search term: {user_data['search_date']}")
    driver.get("https://sauce-demo.myshopify.com/")

    login="//a[text()='Log In']"
    click_element(driver,login)
    if "register" in driver.current_url:
        print("login is successful")
    else:
        print("warning: login page may have not loaded properly current url:", driver.current_url)


    email="//input[@id='customer_email']"
    send_key_to_element(driver,email, user_data['email'])

    pw="//input[@id='customer_password']"
    send_key_to_element(driver,pw, user_data['pw'])

    btn="//input[@value='Sign In']"
    click_element(driver, btn)

    time.sleep(900)

    logout_element=driver.find_element(By.XPATH, "//a[text()='Log Out']")
    if logout_element:
        print("signup sucessfully, u r now in dashboard")

    else:
        print("signup page not loaded")'''



search_item="jacket"
driver.get("https://sauce-demo.myshopify.com/")


    # SEARCH
search = "//input[@id='search-field']"
send_key_to_element(driver, search,search_item)

search_btn = "//input[@id='search-submit']"
wait.until(EC.element_to_be_clickable((By.XPATH, search_btn)))
click_element(driver, search_btn)

if 'search' in driver.current_url:
    print("searched product is shown")
else:
    print("searched prouduct doesnt match with shown product")


    # SELECT PRODUCT
select_item_product = "//a[@id='product-1']"
wait.until(EC.element_to_be_clickable((By.XPATH, select_item_product)))
click_element(driver, select_item_product)

    # ADD TO CART
add_to_cart = "//input[@value='Add to Cart']"
wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart)))
click_element(driver, add_to_cart)


    #checkout first
check_out_link = "//a[@class='checkout']"
click_element(driver, check_out_link)

time.sleep(3)


    #checkout item ra searched item same cha ki nai assert garnu parcha
'''checkout_item="//a[contains(normalize-space(), 'Grey jacket')]"
wait.until(EC.visibility_of_element_located((By.XPATH,checkout_item))).text.strip()
print("Checkout item:", checkout_item)

assert search_item.lower() in checkout_item.lower(),\
    f"Mismatch search page: {search}, Checkout page: {checkout_item}"'''


    # Click on Check Out submit button to complete the purchase
check_out_button = "//input[@id='checkout']"
click_element(driver, check_out_button)


    # Wait before proceeding to next test
time.sleep(5)




driver.quit()