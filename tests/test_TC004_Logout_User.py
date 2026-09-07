from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
import allure

def test_logout_user(driver: WebDriver):
    login_page = LoginPage(driver)
    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Click Signup / Login"):   
        login_page.click_signup_login()
    with allure.step("Verify Login Page"):
        loginheader = login_page.loginverify()
        assert loginheader.is_displayed()
    with allure.step("Enter Valid email"): 
        login_page.enter_email("qareuzzbzczb@example.com")
    with allure.step("Enter Valid Password"):
        login_page.enter_pwd("Password test")
    with allure.step("Click login"):
        login_page.click_login()
    with allure.step("Verify Login"):
        loggedin = login_page.loggedin_indicator()
        assert loggedin.is_displayed()
    with allure.step("Click Logout"):
        login_page.click_logout()
    with allure.step("Verify Logout"):
        loggedout = login_page.logged_out()
        assert loggedout.is_displayed()
    
        