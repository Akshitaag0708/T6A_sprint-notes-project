import pytest

from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.ui
# @pytest.mark.order(2)
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

    logger.info(f"Creating note with title: {note_data['title']}")

    notes_page.create_note(
        category=note_data["category"],
        title=note_data["title"],
        description=note_data["description"]
    )

    assert note_data["title"] in all_titles , "Created note title not found"

    logger.info("Create Note Test Passed")