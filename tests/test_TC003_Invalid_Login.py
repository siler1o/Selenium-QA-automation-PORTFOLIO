import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage

@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.title("TC-003 — Reject invalid login credentials")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login(driver: WebDriver):
    login_page = LoginPage(driver)
    with allure.step("Open Automation Exercise"):
        login_page.goto()
    with allure.step("Click Signup / Login"):   
        login_page.click_signup_login()
    with allure.step("Verify the login section is displayed"):
        login_heading = login_page.loginverify()
        assert login_heading.is_displayed()
    with allure.step("Enter Invalid Account"): 
        login_page.enter_email("negativetest@example.com")
    with allure.step("Enter Invalid Password"):
        login_page.enter_pwd("wrong password")
    with allure.step("Click login"):
        login_page.click_login_wait()
    with allure.step("Incorrect Prompt Message"):
        incorrect_prompt = login_page.email_incorrect()
        assert incorrect_prompt.is_displayed()
    with allure.step("Verify Logged out"):
        indicator = login_page.logged_out_indicator()
        assert indicator.is_displayed()