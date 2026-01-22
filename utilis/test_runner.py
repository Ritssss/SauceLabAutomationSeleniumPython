from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless=new") #UI (browser window) bina Chrome run garcha. Browser open hunna. Background ma automation chalcha


    service = Service(
        "C:\\Users\\Sriza\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    )

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
