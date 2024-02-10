from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to Chrome driver executable
CHROME_DRIVER_PATH = r"C:/Program Files/chromedriver-win64/chromedriver.exe"

# Create a service object
service = Service(CHROME_DRIVER_PATH)

# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()

# Initialize Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a website
driver.get("https://www.saucedemo.com/")
print(driver.title)

# Login
username_input  = driver.find_element(By.ID, 'user-name')
username_input.send_keys("standard_user")
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("secret_sauce")
password_input.send_keys(Keys.RETURN) #Enter key

# clicking element
link = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
link.click()

try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'back-to-products')))
    element.click()
except:
    driver.quit()

try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Sauce Labs Bike Light")))
    element.click()
except:
    driver.quit()

try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'add-to-cart-sauce-labs-bike-light')))
    element.click()
except:
    driver.quit()

# Back to previous page
driver.back()
driver.back()
# Forward
driver.forward()
# clear for textfield since it appends
# element.clear()

# Add a delay to prevent the script from exiting immediately
time.sleep(10)  # Delay for 10 seconds

# Quit the WebDriver
driver.quit()