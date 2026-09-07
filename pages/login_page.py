from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:

  def __init__(self, driver): #my constructor / set up the things it needs
    self.driver = driver #chrome browser driver
    self.wait = WebDriverWait(driver, 10)

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

  def enter_email(self, email):
    self.driver.find_element(
      "css selector", "input[data-qa='login-email']"
    ).send_keys(email)

  def enter_pwd(self, pwd):
    self.driver.find_element(
      "css selector", "input[data-qa='login-password']"
    ).send_keys(pwd)
#clicklogin withou explicit waits
  def click_login(self):
    self.driver.find_element(
      "css selector",
      "button[data-qa='login-button']"
    ).click()
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
    incorrect_prompt = self.wait.until(
        EC.visibility_of_element_located((
           By.XPATH, 
           "//p[text()='Your email or password is incorrect!']")
           )
         )
    return incorrect_prompt
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

  def logged_out(self):
    loggedout = self.wait.until(
      EC.visibility_of_element_located((
           By.LINK_TEXT, 
           "Signup / Login")
        )
    )
    return loggedout