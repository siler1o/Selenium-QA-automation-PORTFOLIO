from selenium import webdriver
from pages.login_page import LoginPage
import allure

def test_invalid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    with allure.step("Open Automation Exercise"):
        login_page.goto()
    with allure.step("Click Signup / Login"):   
        login_page.click_signup_login()
    with allure.step("Enter Invalid email"): 
        login_page.enter_email("negativetest@example.com")
    with allure.step("Enter Invalid Password"):
        login_page.enter_pwd("wrong password")
    with allure.step("Click login"):
        login_page.click_login()
    with allure.step("Incorrect Prompt Message"):
        incorrect_prompt = login_page.email_incorrect()
        assert incorrect_prompt.is_displayed()
    with allure.step("Verify Logged out"):
        indicator = login_page.logged_out_indicator()
        assert indicator.is_displayed()
    driver.quit()
