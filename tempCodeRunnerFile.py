from selenium import webdriver

PATH = "C:/Program Files/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()