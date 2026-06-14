from datetime import datetime
import pytest
import os
from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from utils.data_reader import DataReader
from utils.logger import get_logger
logger = get_logger()

@pytest.mark.ui
@pytest.mark.parametrize("user_type",["invalid_email", "invalid_password"])
def test_invalid_login_ui(browser,user_type):

    logger.info(f"Invalid Login Test Started - {user_type}")

    config = ConfigReader.read_config()
    browser.get(config["qa"]["base_url"])

    login_data = DataReader.read_json("test_data/login_api.json")
    user = login_data[user_type]

    logger.info(f"Trying login with email: {user['email']}")

    login_page = LoginPage(browser)
    login_page.login(
        user["email"],
        user["password"]
    )

    os.makedirs("reports/screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = (f"reports/screenshots/{user_type}_{timestamp}.png")
    browser.save_screenshot(screenshot_path)


    assert "login" in browser.current_url.lower()

    logger.info(f"Invalid Login Test Passed - {user_type}")