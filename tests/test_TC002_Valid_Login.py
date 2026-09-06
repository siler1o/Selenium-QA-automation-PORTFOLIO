from selenium import webdriver
import time

from pages.login_page import LoginPage

def test_login_user():

    driver = webdriver.Chrome() #opens chrome

    driver.get("https://automationexercise.com")

    time.sleep(5) #wait for 5 seconds then proceeds to the next command/code

    driver.find_element("link text", "Signup / Login").click() #HOW, WHAT

    time.sleep(3) 

    assert "Login to your account" in driver.page_source #assertion checkpoint

    login_page = LoginPage(driver)
    login_page.enter_email("qareuzzbzczb@example.com")
    login_page.enter_pwd("Password test")
    login_page.click_login()

    logout = driver.find_element(
        "link text", 
        "Logout") #validation checkpoint to check if the logout button is displayed after login
    assert logout.is_displayed() 

    time.sleep(5) 

    driver.quit()