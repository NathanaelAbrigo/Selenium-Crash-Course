# from selenium import webdriver

# PATH = "C:/Program Files/chromedriver-win64/chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# driver.get("https://techwithtim.net")
# print(driver.title)
# driver.quit()

## ChatGPT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to Chrome driver executable
CHROME_DRIVER_PATH = r"C:/Program Files/chromedriver-win64/chromedriver.exe"

# Create a service object
service = Service(CHROME_DRIVER_PATH)

# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window

# Initialize Chrome WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a website
driver.get("https://techwithtim.net")
print(driver.title)

# Quit the WebDriver
driver.quit()
