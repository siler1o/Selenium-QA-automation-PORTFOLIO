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

        product_url = view_product.get_attribute("href")
        view_product.click()

        if "#google_vignette" in self.driver.current_url:
            self.driver.get(product_url)

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
