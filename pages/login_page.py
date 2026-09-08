from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
  
  invalid_message = "Your email or password is incorrect!"

  def __init__(self, driver): #my constructor / set up the things it needs
    self.driver = driver #chrome browser driver
    self.wait = WebDriverWait(driver, 10)
    self.home_url = "https://automationexercise.com/"

  def goto(self):
    self.driver.get("https://automationexercise.com")

  def loginverify(self):
     loginheader = self.wait.until(
       EC.visibility_of_element_located((
          By.XPATH, 
          "//h2[text()='Login to your account']")
          )
     )
     return loginheader
  
  def newuserverify(self):
     signupheader = self.wait.until(
       EC.visibility_of_element_located((
          By.XPATH, 
          "//h2[text()='New User Signup!']")
          )
     )
     return signupheader

#email insertion
  def enter_email(self, email):
    self.driver.find_element(
      "css selector", "input[data-qa='login-email']"
    ).send_keys(email)

#name insertion with ec
  def insert_name(self, name):
    name_field = self.wait.until(
      EC.visibility_of_element_located((
        By.CSS_SELECTOR, "input[data-qa='signup-name']")
        )
    )
    name_field.send_keys(name)

#email insertion with ec
  def insert_email(self, email):
    email_field = self.wait.until(
      EC.visibility_of_element_located((
        By.CSS_SELECTOR, "input[data-qa='signup-email']")
        )
    )
    email_field.send_keys(email)
    
#enterpwd without ec
  def enter_pwd(self, pwd):
    self.driver.find_element(
      "css selector", "input[data-qa='login-password']"
    ).send_keys(pwd)
#clicklogin withou ec

  def click_login(self):
    self.driver.find_element(
      "css selector",
      "button[data-qa='login-button']"
    ).click()

#click signup with EC
  def click_signup_wait(self):
    signup_button = self.wait.until(
        EC.element_to_be_clickable((
          By.CSS_SELECTOR, 
          "button[data-qa='signup-button']")
            )
        )
    signup_button.click()

#clicklogin with EC
  def click_login_wait(self):
    login_button = self.wait.until(
        EC.element_to_be_clickable((
          By.CSS_SELECTOR, 
          "button[data-qa='login-button']")
            )
        )
    login_button.click()

#click signup with EC
  def click_signup_login(self):
    signup_login = self.wait.until(
        EC.element_to_be_clickable((
            By.LINK_TEXT, 
            "Signup / Login")
            )
         )
    signup_login.click()
#invalid sign in assertion
  def email_incorrect(self):
        return self.wait.until(
            EC.visibility_of_element_located((
              By.XPATH,
              f"//p[text()='{self.invalid_message}']")
            )
         )
  
#invalid sign up assertion/validation
  def user_exist(self):
    exist_prompt = self.wait.until(
        EC.visibility_of_element_located((
           By.XPATH, 
           "//p[text()='Email Address already exist!']")
           )
         )
    return exist_prompt
  
#verify logged out
  def logged_out_indicator(self):
    indicator = self.wait.until(
        EC.visibility_of_element_located((
           By.LINK_TEXT, 
           "Signup / Login")
           )
         )
    return indicator
  
#logoutclick
  def click_logout(self):
    logout = self.wait.until(
        EC.element_to_be_clickable((
           By.LINK_TEXT,
           "Logout")
           )
         )
    logout.click()

#loggedin assertion
  def loggedin_indicator(self):
    loggedin = self.wait.until(
      EC.visibility_of_element_located((
        By.LINK_TEXT, "Logout")
        )
    )
    return loggedin
  
#loggedout assertion
  def logged_out(self):
    loggedout = self.wait.until(
      EC.visibility_of_element_located((
           By.LINK_TEXT, 
           "Signup / Login")
        )
    )
    return loggedout
