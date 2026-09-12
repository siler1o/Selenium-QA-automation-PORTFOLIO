import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.navigation_bar import NavigationBar
from pages.contact_us import ContactUs
from pages.products_page import ProductPage


@allure.feature("Shopping Cart")
@allure.story("Add two products to the cart")
@allure.title("TC-012 — Verify products, prices, quantities, and totals in cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_products_to_cart(driver: WebDriver):
    login_page = LoginPage(driver)
    products_page = ProductPage(driver)
    contact_us = ContactUs(driver)
    navigation_bar = NavigationBar(driver)

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Verify Homepage"):
        assert contact_us.verify_home()
    with allure.step("Click Product Page"):
        navigation_bar.click_product()
    with allure.step("Verify All Products heading is displayed"):
        all_product_header = products_page.product_header()
        assert all_product_header.is_displayed()
    with allure.step("Save the first product's listing price"):
        expected_first_price = products_page.first_listing_price().text.strip()
        expected_second_price = products_page.second_listing_price().text.strip()
    with allure.step("Hover over first product and click 'Add to cart'"):
        products_page.click_add_one()
    with allure.step("Click 'Continue Shopping' button"):
        products_page.continue_shopping()
    with allure.step("Hover over the second product and select Add to cart"):
        products_page.click_add_two()
    with allure.step("Select View Cart in the confirmation"):  
        products_page.view_cart()
    with allure.step("Check the carts product names"):   
        details_one = products_page.product_one_details()
        details_two = products_page.product_two_details()
        assert details_one.is_displayed()
        assert details_two.is_displayed()
    with allure.step("Verify cart unit prices"):
        first_price = products_page.price_one()
        second_price = products_page.price_two()
        assert first_price.is_displayed()
        assert first_price.text.strip() == expected_first_price
        assert second_price.is_displayed()
        assert second_price.text.strip() == expected_second_price
    with allure.step("Verify cart quantities"):
        first_quantity = products_page.first_cart_quantity()
        second_quantity = products_page.second_cart_quantity()
        assert first_quantity.text.strip() == "1"
        assert second_quantity.text.strip() == "1"
    with allure.step("Verify cart product total"):
        first_total = products_page.first_cart_total()
        second_total = products_page.second_cart_total()
        assert first_total.text.strip() == expected_first_price
        assert second_total.text.strip() == expected_second_price


        
