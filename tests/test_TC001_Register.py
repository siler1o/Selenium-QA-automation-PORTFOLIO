from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#TC-001 - Registration of USER hehe

def test_register_user():

    driver = webdriver.Chrome()

    driver.get("https://automationexercise.com")

    time.sleep(2)

    driver.find_element("link text", "Signup / Login").click()

    time.sleep(2)

    assert "New User Signup!" in driver.page_source

    driver.find_element("name", "name").send_keys("Reuben QA tester")

    driver.find_element("css selector", "input[data-qa='signup-email']").send_keys("qarzcab@example.com")

    time.sleep(2)

    driver.find_element("css selector", "button[data-qa='signup-button']").click()

    time.sleep(2)

    assert "Enter Account Information" in driver.page_source

    driver.find_element("css selector", "label[for='id_gender1']").click()

    driver.find_element("css selector", "input[data-qa='password']").send_keys("Password test")

    #dob below / also change made it cleaner below.

    #select is a class that is used to select dropdowns in selenium. you need to import it first from selenium.webdriver.support.ui import Select
    daydropdown = Select(driver.find_element("id", "days"))
    daydropdown.select_by_value("31")

    monthdropdown = Select(driver.find_element("name", "months"))
    monthdropdown.select_by_visible_text("July")

    yeardropdown = Select(driver.find_element("css selector", "select[data-qa='years']"))
    yeardropdown.select_by_value("2001")

    #checkbox additional info i learned. "strategy" , "value" is the term

    signupcheckbox1 = driver.find_element("name", "newsletter")
    signupcheckbox1.click()

    signupcheckbox2 = driver.find_element("id", "optin")
    signupcheckbox2.click()

    firstname = driver.find_element("css selector", "#first_name")
    firstname.send_keys("Reuben the QA")

    lastname = driver.find_element("id", "last_name")
    lastname.send_keys("Test")

    company = driver.find_element("css selector", "[data-qa='company']")
    company.send_keys("Freelance Company")

    address1 = driver.find_element("css selector","input[data-qa='address']")
    address1.send_keys("philippines, test address, best company")

    address2 = driver.find_element("name", "address2")
    address2.send_keys("the test address part 2")

    countrydropdown = Select(driver.find_element("id" , "country"))
    countrydropdown.select_by_value("Singapore")

    state = driver.find_element("css selector", "input[data-qa='state']")
    state.send_keys("Test state philippines")

    city = driver.find_element("id", "city")
    city.send_keys("Manila city")

    zipcode = driver.find_element("name", "zipcode")
    zipcode.send_keys("1234")

    mobnum = driver.find_element("css selector", "#mobile_number")
    mobnum.send_keys("09711224400")

    time.sleep(2) #timer to display

    createaccount = driver.find_element("css selector", "button[data-qa='create-account']")
    createaccount.click()

    time.sleep(2)

    driver.quit()

