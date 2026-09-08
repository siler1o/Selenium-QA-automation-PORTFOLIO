from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.navigation_bar import MenuBar
import allure

def test_Testnavicase(driver: WebDriver):
    login_page = LoginPage(driver)
    navigation_bar = MenuBar(driver)
    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Click Test Cases"):
        navigation_bar.click_testcase()
    with allure.step("Verify Test Case Page"):
        test_case_header = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((
            By.XPATH, "//h2[normalize-space()='Test Cases']")
            )
        )
        assert test_case_header