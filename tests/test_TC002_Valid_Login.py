import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage


@allure.feature("Authentication")
@allure.story("Valid Login")
@allure.title("TC-002 — Login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_user(driver: WebDriver):
    login_page = LoginPage(driver)

    with allure.step("Open the Automation Exercise website"):
        login_page.goto()

    with allure.step("Open the Signup / Login page"):
        login_page.click_signup_login()

    with allure.step("Verify the login section is displayed"):
        login_heading = login_page.loginverify()
        assert login_heading.is_displayed()

    with allure.step("Enter valid login credentials"):
        login_page.enter_email("qareuzzbzczb@example.com")
        login_page.enter_pwd("Password test")

    with allure.step("Submit the login form"):
        login_page.click_login_wait()

    with allure.step("Verify the user is successfully logged in"):
        logout_link = login_page.loggedin_indicator()
        assert logout_link.is_displayed(), (
            "Logout link was not displayed after login")