from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
import allure

@allure.feature("Authentication")
@allure.story("Duplicate Registration")
@allure.title("TC-005 — Reject registration with an existing email")
@allure.severity(allure.severity_level.NORMAL)
def test_register_with_existing_email(driver: WebDriver):
    login_page = LoginPage(driver)
    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Click Signup / Login"):   
        login_page.click_signup_login()
    with allure.step("Verify Signup page"):
        signupheader = login_page.newuserverify()
        assert signupheader.is_displayed()
    with allure.step("Enter a valid name"):
        login_page.insert_name("Reuben QA Test")
    with allure.step("Enter a registered Email"):
        login_page.insert_email("qareuzzbzczb@example.com")
    with allure.step("Click Signup"):
        login_page.click_signup_wait()
    with allure.step("User Exist Promp"):
        exist_prompt = login_page.user_exist()
        assert exist_prompt.is_displayed()
    with allure.step("Verify Signup page"):
        signupheader = login_page.newuserverify()
        assert signupheader.is_displayed()
        assert "/signup" in driver.current_url 
    

    