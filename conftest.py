import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver #run test 

    driver.quit()