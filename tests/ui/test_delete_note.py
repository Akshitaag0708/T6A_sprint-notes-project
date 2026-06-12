import pytest

from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.ui
@pytest.mark.order(4)
def test_delete_note(browser):

    logger.info("Delete Note Test Started")

    config = ConfigReader.read_config()

    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("Logging into application")

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    logger.info("Deleting note")

    notes_page.delete_note()

    notes_page.refresh_page()

    all_titles = notes_page.get_all_note_titles()

    logger.info(
        f"Remaining Notes: {all_titles}"
    )

    assert (
        config["qa"]["note"]["title"]
        not in all_titles
    ), "Deleted note still visible"

    logger.info("Delete Note Test Passed")