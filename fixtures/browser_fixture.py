import pytest
from selenium.webdriver import Chrome, ChromeOptions
from config.config_reader import ConfigReader


@pytest.fixture(scope="function")
def browser():

    config = ConfigReader.read_config()

    options = ChromeOptions()
    options.add_argument("--disable-notifications")
    # options.add_argument("--disable-popup-blocking")
    # options.add_argument("--disable-infobars")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # prefs = {
    #     "profile.default_content_setting_values.notifications": 2
    # }
    # options.add_experimental_option(
    #     "prefs",
    #     prefs
    # )
    driver = Chrome(options=options)

    driver.maximize_window()

    driver.get(config["qa"]["base_url"])

    yield driver

    driver.quit()