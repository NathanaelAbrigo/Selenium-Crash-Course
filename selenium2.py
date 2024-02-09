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
# changed website since old one does not have input elements
driver.get("https://www.saucedemo.com/")
print(driver.title)

# Find the username input field by name and enter the username
# hierarchy to get element => id, name, class
username_input  = driver.find_element(By.ID, 'user-name')
username_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("secret_sauce")

password_input.send_keys(Keys.RETURN) #Enter key

#This is to take account the loading of the website.
try:
    print("here")
    inventory_container = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'inventory_container')))

    #getting all inventory items
    inventory_items = inventory_container.find_elements(By.CLASS_NAME,'inventory_item')

    #specific going to item name 
    for item in inventory_items:
        item_name = item.find_element(By.CLASS_NAME, 'inventory_item_name')
        print(item_name.text)

    # print(inventory_container.text)
except:
    driver.quit()



