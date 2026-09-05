from selenium import webdriver
import time

driver = webdriver.Chrome() #opens chrome

driver.get("https://automationexercise.com")

print(driver.title) #print the title of the page in the terminal

time.sleep(5) #wait for 5 seconds then proceeds to the next command/code

driver.find_element("link text", "Signup / Login").click() #HOW, WHAT

time.sleep(3) 

assert "Login to your account" in driver.page_source

driver.find_element("name", "email").send_keys("testuser@example.com")

driver.quit()