from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:
    ALL_PRODUCTS_HEADING = (
        By.XPATH,
        "//h2[normalize-space()='All Products']"
    )
    PRODUCT_LIST = (By.CLASS_NAME, "productinfo")
    VIEW_PRODUCT = (By.LINK_TEXT, "View Product")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product-information h2")
    PRODUCT_INFORMATION = (By.CSS_SELECTOR, "div.product-information")
    SEARCH_BAR = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_HEADER = (
    By.XPATH,
    "//h2[text()='Searched Products']"
    )

    def __init__(self, driver):
     self.driver = driver
     self.wait = WebDriverWait(driver, 10)

    def product_header (self):
        return self.wait.until(
            EC.visibility_of_element_located(
               self.ALL_PRODUCTS_HEADING
            )
        )

    def product_list(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located(
                self.PRODUCT_LIST
            )
        )

    def click_product(self):
        view_product = self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_PRODUCT
            )
        )
        view_product.click()

    def product_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_TITLE
            )
        )

    def product_details(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_INFORMATION
            )
        )

    def type_search(self, search):
        search_type = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BAR
            )
        )
        search_type.send_keys(search)

    def click_search(self):
        click_search_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        )
        click_search_button.click()

    def search_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_HEADER
            )
        )


