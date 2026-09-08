from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ContactUs:

    def __init__(self, driver): #my constructor / automatic setup method
     self.driver = driver #chrome browser driver
     self.wait = WebDriverWait(driver, 10)   

 #click contactus with EC
    def click_contact_us(self):
     contact_us = self.wait.until(
        EC.element_to_be_clickable((
            By.LINK_TEXT, 
            "Contact us")
            )
         )
     contact_us.click()
#get in touch assertion
    def touch_assertion(self):
     contactpage = self.wait.until(
        EC.visibility_of_element_located((
           By.XPATH, 
           "//h2[text()='Get In Touch']")
            )
        )
     return contactpage

#enter name and type
    def enter_name(self, name):
      name_field = self.wait.until(
        EC.visibility_of_element_located((
         By.NAME,
         "name")
         )
      )
      name_field.send_keys(name)
#enter email and type
    def enter_email(self, email):
      name_field = self.wait.until(
        EC.visibility_of_element_located((
         By.NAME, 
         "email")
         )
      )
      name_field.send_keys(email)
#enter subject and type      
    def enter_subject(self, subject):
      subject_field = self.wait.until(
        EC.visibility_of_element_located((
         By.NAME,
         "subject")
         )
      )
      subject_field.send_keys(subject)
#enter message and type
    def enter_message(self, message):
      message_field = self.wait.until(
        EC.visibility_of_element_located((
         By.NAME, "message")
         )
      )
      message_field.send_keys(message)
#choose file
    def upload_file (self, file):
      file_field = self.wait.until(
        EC.presence_of_element_located((
         By.CSS_SELECTOR, 
         "input[name='upload_file']")
         )
      )
      file_field.send_keys(file)
#click ok alert
    def accept_alert(self):
      alert = self.wait.until(
        EC.alert_is_present(
         )
      )
      alert.accept()
#click submit
    def click_submit(self):
      submit_button = self.wait.until(
        EC.element_to_be_clickable((
         By.NAME, 
         "submit")
         )
      )
      submit_button.click()
#verify success prompt
    def success_prompt(self):
      success_message = self.wait.until(
        EC.visibility_of_element_located((
         By.CSS_SELECTOR, 
         "div.status.alert.alert-success")
         )
      )
      return success_message
#return home
    def click_home(self):
      return_home = self.wait.until(
        EC.element_to_be_clickable((
          By.LINK_TEXT, 
          "Home"
        ))
      )
      return_home.click()
#verify homepage with link
    def verify_home(self):
      return self.driver.current_url == self.home_url