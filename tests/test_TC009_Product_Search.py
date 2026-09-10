import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.navigation_bar import NavigationBar
from pages.contact_us import ContactUs
from pages.products_page import ProductPage


@allure.feature("Products")
@allure.story("Search for a product")
@allure.title("TC-009 — Verify Product Search")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_product(driver: WebDriver):
    login_page = LoginPage(driver)
    navigation_bar = NavigationBar(driver)
    contact_us = ContactUs(driver)
    products_page = ProductPage(driver)
    search_term = "Blue Top"

    with allure.step("Open Automation Exercise Website"):
        login_page.goto()
    with allure.step("Verify Homepage"):
        assert contact_us.verify_home()
    with allure.step("Click Product Page"):
        navigation_bar.click_product()
    with allure.step("Verify All Products heading is displayed"):
        all_product_header = products_page.product_header()
        assert all_product_header.is_displayed()
    with allure.step("Enter a product name in the search field"):
        products_page.type_search("Blue Top")
    with allure.step("Click Search Button"):
        products_page.click_search()
    with allure.step("Verify the searched products section"):
        product_header = products_page.search_header()
        assert product_header.is_displayed()
    with allure.step("Verify the products are related to the search"):
        searched_products = products_page.product_list()
        assert len(searched_products) > 0, "No searched products were displayed"
        assert all(search_term.lower() in product.text.lower()
        for product in searched_products
        ), "An unrelated product was displayed"