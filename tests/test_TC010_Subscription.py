import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.navigation_bar import NavigationBar
from pages.contact_us import ContactUs
from pages.products_page import ProductPage


@allure.feature("Subscription")
@allure.story("Subscribe from the homepage")
@allure.title("TC-010 — Verify Subscription on Homepage")
@allure.severity(allure.severity_level.NORMAL)
def test_search_product(driver: WebDriver):
    login_page = LoginPage(driver)
    products_page = ProductPage(driver)
    contact_us = ContactUs(driver)

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Verify Homepage"):
        assert contact_us.verify_home()
    with allure.step("Scroll to the footer"):
        scroll_down = login_page.scroll_to_subscription()
    with allure.step("Verify the subscription heading"):
        heading = login_page.subscription_header()
        assert heading.is_displayed()
    with allure.step("Verify the subscription heading"):
        heading = login_page.subscription_header()
        assert heading.is_displayed()
    with allure.step("Enter a valid email in the subscription field"):
        login_page.enter_subemail("qareuzzbzczb@example.com")
    with allure.step("Click the arrow button beside the email field"):
        login_page.click_subscribe()
    with allure.step("Verify the confirmation message"):
        message_popup = login_page.success_message()
        assert message_popup.is_displayed()
        assert message_popup.text.strip() == "You have been successfully subscribed!"

