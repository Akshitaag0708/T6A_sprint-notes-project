import pytest

from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.ui
@pytest.mark.order(1)
def test_login(browser):

    logger.info("Login Test Started")

    config = ConfigReader.read_config()

    env = config["qa"]

    login_page = LoginPage(browser)

    logger.info(
        f"Attempting login with user: {env['email']}"
    )

    login_page.login(
        env["email"],
        env["password"]
    )

    logger.info(
        f"Current URL after login: {browser.current_url}"
    )

    assert "notes/app" in browser.current_url

    logger.info("Login Test Passed")