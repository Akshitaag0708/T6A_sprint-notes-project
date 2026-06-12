import pytest

from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.ui
@pytest.mark.order(2)
def test_create_note(browser):

    logger.info("Create Note Test Started")

    config = ConfigReader.read_config()

    note_data = config["qa"]["note"]

    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("Logging into application")

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    logger.info(
        f"Creating note with title: {note_data['title']}"
    )

    notes_page.create_note(
        category=note_data["category"],
        title=note_data["title"],
        description=note_data["description"]
    )

    actual_title = (
        notes_page.get_created_note_title()
    )

    actual_description = (
        notes_page.get_created_note_description()
    )

    logger.info(
        f"Created Title: {actual_title}"
    )

    logger.info(
        f"Created Description: {actual_description}"
    )

    assert actual_title == note_data["title"]

    assert actual_description == note_data["description"]

    logger.info("Create Note Test Passed")