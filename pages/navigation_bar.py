from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class NavigationBar:
    TEST_CASES_LINK = (By.LINK_TEXT, "Test Cases")
    TEST_CASES_HEADING = (
        By.XPATH,
        "//h2[normalize-space()='Test Cases']"
    )

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)

    def click_test_cases(self):
        test_cases_link = self.wait.until(
            EC.element_to_be_clickable(
                self.TEST_CASES_LINK
            )
        )
        test_cases_link.click()

    def get_test_cases_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.TEST_CASES_HEADING
            )
        )