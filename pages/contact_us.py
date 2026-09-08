from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ContactUs:
    
    CONTACT_US_LINK = (By.LINK_TEXT, "Contact us")
    GET_IN_TOUCH_HEADING = (
        By.XPATH,
        "//h2[normalize-space()='Get In Touch']"
    )
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    SUBJECT_FIELD = (By.NAME, "subject")
    MESSAGE_FIELD = (By.NAME, "message")
    UPLOAD_FIELD = (
        By.CSS_SELECTOR,
        "input[name='upload_file']"
    )
    SUBMIT_BUTTON = (By.NAME, "submit")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "div.status.alert.alert-success"
    )
    HOME_LINK = (By.LINK_TEXT, "Home")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.home_url = "https://automationexercise.com/"

    def click_contact_us(self):
        contact_us_link = self.wait.until(
            EC.element_to_be_clickable(self.CONTACT_US_LINK)
        )
        contact_us_link.click()

    def touch_assertion(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.GET_IN_TOUCH_HEADING
            )
        )

    def enter_name(self, name):
        name_field = self.wait.until(
            EC.visibility_of_element_located(
                self.NAME_FIELD
            )
        )
        name_field.send_keys(name)

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL_FIELD
            )
        )
        email_field.send_keys(email)

    def enter_subject(self, subject):
        subject_field = self.wait.until(
            EC.visibility_of_element_located(
                self.SUBJECT_FIELD
            )
        )
        subject_field.send_keys(subject)

    def enter_message(self, message):
        message_field = self.wait.until(
            EC.visibility_of_element_located(
                self.MESSAGE_FIELD
            )
        )
        message_field.send_keys(message)

    def upload_file(self, file_path):
        upload_field = self.wait.until(
            EC.presence_of_element_located(
                self.UPLOAD_FIELD
            )
        )
        upload_field.send_keys(file_path)

    def click_submit(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        )
        submit_button.click()

    def accept_alert(self):
        alert = self.wait.until(
            EC.alert_is_present()
        )
        alert.accept()

    def success_prompt(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )

    def click_home(self):
        home_link = self.wait.until(
            EC.element_to_be_clickable(
                self.HOME_LINK
            )
        )
        home_link.click()

    def verify_home(self):
        return self.wait.until(
            EC.url_to_be(self.home_url)
        )