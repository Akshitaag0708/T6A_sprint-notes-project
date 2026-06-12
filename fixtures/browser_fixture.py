import pytest
from selenium.webdriver import Chrome, ChromeOptions
from config.config_reader import ConfigReader


@pytest.fixture(scope="function")
def browser():

    config = ConfigReader.read_config()

    options = ChromeOptions()

    driver = Chrome(options=options)

    driver.maximize_window()

    driver.get(config["qa"]["base_url"])

    yield driver

    driver.quit()