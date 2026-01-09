from selenium import webdriver
from selenium.webdriver.chrome.service import Service #Specifies ChromeDriver path & manages its process
from selenium.webdriver.chrome.options import Options #Options is used to customize the Chrome browser behavior before launching it.
from selenium.webdriver.common.by import By
import time
import allure

chrome_options=Options()
chrome_options.add_argument("--start-maximized")

#location of chromedrive
service = Service("C:\\Users\\Sriza\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")


#initialize the driver
driver=webdriver.Chrome(service=service, options=chrome_options) #use garna ko lagi bhitra lekheko lekhni


def click_element(driver, a):
    element=driver.find_element(By.XPATH, a)
    element.click()


def send_key_to_element(driver, xpath, key):
    element=driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(key)

def get_text(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text.strip()

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


search_input = "//input[@id='search-field']"
send_key_to_element(driver, search_input, search_item)

search_btn = "//input[@id='search-submit']"
click_element(driver, search_btn)
time.sleep(2)

if "search" in driver.current_url:
    print("Search page loaded")
else:
    print("Search page not loaded correctly")

# ----------------- SELECT PRODUCT -----------------
select_product = "//a[@id='product-1']"
click_element(driver, select_product)
time.sleep(2)

# ----------------- GET PRODUCT NAME -----------------
product_title_xpath = "//h1"
product_name = get_text(driver, product_title_xpath)
print("product selected:", product_name)
'''Use //h1 on product detail page. Use <h3> or <a> on search results or listing page.'''

# ----------------- ADD TO CART -----------------
add_to_cart_btn = "//input[@value='Add to Cart']"
click_element(driver, add_to_cart_btn)
time.sleep(2)
print("Product added to cart")

# ----------------- GO TO CART / CHECKOUT -----------------
checkout_link = "//a[@class='checkout']"
click_element(driver, checkout_link)
time.sleep(2)

# ----------------- GET CART PRODUCT NAME -----------------
checkout_item_xpath = f"//a[contains(normalize-space(),'Grey jacket')]"
checkout_item = get_text(driver, checkout_item_xpath)
print("Checkout item:", checkout_item)

# ----------------- ASSERTION -----------------
if product_name.lower() in checkout_item.lower():
    print("Assertion passed: Product matches from product page to cart")
else:
    print(f"Assertion failed! Product Page: {product_name}, Checkout Page: {checkout_item}")

# ----------------- CLICK FINAL CHECKOUT BUTTON -----------------
check_out_button = "//input[@value='Check Out' and @id='checkout']"
click_element(driver, check_out_button)
time.sleep(2)
print("Clicked on final checkout")

# ----------------- CLOSE DRIVER -----------------
driver.quit()
print("Test completed successfully")