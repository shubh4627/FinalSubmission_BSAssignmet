import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread

BROWSERSTACK_USERNAME =  "shubhijain_ygvYhG"
BROWSERSTACK_ACCESS_KEY =  "U8MxHehLyEAitKU8Wj9b"
URL = "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "ShubhiJain_Assignment"
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest-beta",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel", # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "Edge",
        "browserVersion": "106.0",
        "os": "OS X",
        "osVersion": "Monterey",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },

   
]

def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())

def run_session(cap):
    bstack_options = {
        "osVersion" : cap["osVersion"],
        "buildName" : cap["buildName"],
        "sessionName" : cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    print(options)
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(command_executor=URL, options=options)
    driver.get("https://flipkart.com/")
    driver.maximize_window()
    driver.find_element("xpath", "//button[contains(text(),'✕')]").click()
    WebDriverWait(driver, 10)
    driver.find_element('xpath', '//input[@name="q" and @placeholder="Search for products, brands and more"]').click()
    driver.find_element('xpath', '//input[@name="q" and @placeholder="Search for products, brands and more"]').send_keys("Samsung Galaxy S10")
    driver.find_element('xpath', '//button[@type="submit"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="_10Ermr" and contains(text(),"results for ")]')))
    driver.find_element('xpath','//a[@href="/mobiles/pr?sid=tyy,4io&q=Samsung+Galaxy+S10&otracker=categorytree" and @title="Mobiles"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@title="SAMSUNG"]//input[@type="checkbox"]//following-sibling::div[1]')))
    driver.find_element('xpath','//div[@title="SAMSUNG"]//input[@type="checkbox"]//following-sibling::div[1]').click()

    element = driver.find_element('xpath', '//div[contains(text(),"Customer Ratings")]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    driver.find_element('xpath', '//img[@src="//static-assets-web.flixcart.com/fk-p-linchpin-web/fk-cp-zion/img/fa_62673a.png"]/../../..//input//following-sibling::div[1]').click()
    time.sleep(5)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_10UF8M" and text()="Price -- High to Low"]')))

    driver.find_element('xpath', '//div[@class="_10UF8M" and text()="Price -- High to Low"]').click()

    time.sleep(5)

    try:
            name_list = []
            for element0 in driver.find_elements('xpath','//div[@class="_1YokD2 _3Mn1Gg"]//div[@class="_1AtVbE col-12-12"]//div[@class="_4rR01T"]'):
                name = element0.text
                name_list.append(name)
            print(name_list)
    except Exception:
        print("Exception")

    try:
            price_list = []
            for element1 in driver.find_elements('xpath','//div[@class="_1YokD2 _3Mn1Gg"]//div[@class="_1AtVbE col-12-12"]//div[@class="_30jeq3 _1_WHN1"]'):
                price = element1.text
                price_list.append(price)
            print(price_list)
    except Exception:
            print("Exception")
    try:
            link_list = []
            for element2 in driver.find_elements('xpath','//div[@class="_1YokD2 _3Mn1Gg"]//div[@class="_1AtVbE col-12-12"]//a[@class="_1fQZEK"]'):
                link = element2.get_attribute("href")
                link_list.append(link)
            print(link_list)
    except Exception:
            print("Exception")
    driver.quit()

for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()