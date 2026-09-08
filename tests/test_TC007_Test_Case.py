import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.navigation_bar import NavigationBar


@allure.feature("Navigation")
@allure.story("Test Cases Page")
@allure.title("TC-007 — Verify the Test Cases page")
@allure.severity(allure.severity_level.MINOR)
def test_test_cases_page(driver: WebDriver):
    login_page = LoginPage(driver)
    navigation_bar = NavigationBar(driver)
    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Click Test Cases"):
        navigation_bar.click_test_cases()
    with allure.step("Verify the Test Cases page is displayed"):
        test_cases_heading = navigation_bar.get_test_cases_heading()
        assert test_cases_heading.is_displayed()
        assert "TEST CASES" in test_cases_heading.text.upper()
        assert "/test_cases" in driver.current_url