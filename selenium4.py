from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)

# will wait 5 seconds before next line to take account loading time
driver.implicitly_wait(5)

# select language, if u did not select the accept cookies, this will always pop in test runs
language = driver.find_element(By.ID, "langSelect-EN")
language.click()

# will wait 10 seconds before next line
driver.implicitly_wait(10)

cookie = driver.find_element(By.ID, 'bigCookie')
cookie_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)

# Perform multiple clicks on the cookie
for i in range(50):
    actions.click(cookie)
    actions.perform()
    time.sleep(1)  # Add a delay to observe the effects
    cookie = driver.find_element(By.ID, 'bigCookie')  # Re-select the cookie element since it also updates

    count = int(cookie_count.text.split(" ")[0])
    # count = cookie_count.text
    # print(count)
    
    # auto buy items
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


time.sleep(10)