#importstatements
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.contact_us import ContactUs
import allure
from pathlib import Path 

def test_Contact_Us(driver: WebDriver):
    login_page = LoginPage(driver)
    contact_us = ContactUs(driver)
    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Click Contact Us"):
        contact_us.click_contact_us()
    with allure.step("Verify Contact Page"):
        contactpage = contact_us.touch_assertion()
        assert contactpage.is_displayed()
    with allure.step("Enter Name"):
        contact_us.enter_name("Reuben QA Test")
    with allure.step("Enter Email"): 
        contact_us.enter_email("qareuzzbzczb@example.com")
    with allure.step("Enter Subject"):
        contact_us.enter_subject("Example subject test")
    with allure.step("Enter Message"):
        contact_us.enter_message("Hi this is a test only")
    with allure.step("Upload File"):    
        file_field = Path("test_data/attachment test.png").resolve()
        contact_us.upload_file(str(file_field))
    with allure.step("Click Submit"):
        contact_us.click_submit()
    with allure.step("Accept Alert"):
        contact_us.accept_alert()
    with allure.step("Verify Success Message"):
        success_message = contact_us.success_prompt()
        assert success_message.is_displayed()
    with allure.step("Click Home"):
        contact_us.click_home()
    with allure.step("Verify Homepage"):
        assert contact_us.verify_home_url()