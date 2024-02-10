import unittest
from selenium import webdriver
import page

from selenium.webdriver.chrome.service import Service

class PythonOrgSearch(unittest.TestCase):

    #like init
    def setUp(self):
        print("setup")
        CHROME_DRIVER_PATH = r"C:/Program Files/chromedriver-win64/chromedriver.exe"
        service = Service(CHROME_DRIVER_PATH)
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://www.python.org/")
    
    # def test_title(self):
    #     mainPage = page.MainPage()
    #     assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()