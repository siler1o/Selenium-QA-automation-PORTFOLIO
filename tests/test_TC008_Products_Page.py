import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.navigation_bar import NavigationBar
from pages.contact_us import ContactUs
from pages.products_page import ProductPage


@allure.feature("Products")
@allure.story("View product details")
@allure.title("TC-008 — Verify All Products and product detail page")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_page(driver: WebDriver):
    login_page = LoginPage(driver)
    navigation_bar = NavigationBar(driver)
    contact_us = ContactUs(driver)
    products_page = ProductPage(driver)

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Verify Homepage"):
        assert contact_us.verify_home()
    with allure.step("Click Product Page"):
        navigation_bar.click_product()
    with allure.step("Verify All Products heading is displayed"):
        all_product_header = products_page.product_header()
        assert all_product_header.is_displayed()
    with allure.step("Verify product listing is visible"):
        products_cards = products_page.product_list()
        assert len(products_cards) > 0
    with allure.step("Click View Product on the first product"):
        products_page.click_product()
    with allure.step("Verify the first product detail page opens"):
        assert "/product_details/1" in driver.current_url
    with allure.step("Verify the product detail page"):
        product_header = products_page.product_title()
        assert product_header.is_displayed()
        assert product_header.text.strip() == "Blue Top"
    with allure.step("Verify Product details"):
        product_info = products_page.product_details()
        assert product_info.is_displayed()
        details_text = " ".join(product_info.text.split())
        assert "Category: Women > Tops" in details_text
        assert "Rs. 500" in details_text
        assert "Availability: In Stock" in details_text
        assert "Condition: New" in details_text
        assert "Brand: Polo" in details_text




