from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MenuBar:
    def __init__(self, driver): #my constructor / automatic setup method
     self.driver = driver #chrome browser driver
     self.wait = WebDriverWait(driver, 10)   
     self.home_url = "https://automationexercise.com/"
#click test case 
    def click_testcase(self):
         test_case = self.wait.until(
              EC.element_to_be_clickable((
                By.LINK_TEXT, "Test Cases" )
                )
             )
         test_case.click()
