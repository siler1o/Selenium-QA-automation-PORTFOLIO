import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    # Prevent third-party ads from interrupting practice-site tests
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd(
        "Network.setBlockedURLs",
        {
            "urls": [
                "*://*.googlesyndication.com/*",
                "*://*.doubleclick.net/*",
                "*://*.googleadservices.com/*",
            ]
        },
    )

    yield driver
    driver.quit()