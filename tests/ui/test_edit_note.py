import pytest
from time import sleep

from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.config_reader import ConfigReader
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.ui
@pytest.mark.order(3)
def test_edit_note(browser):

    logger.info("Edit Note Test Started")

    config = ConfigReader.read_config()

    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("Logging into application")

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    logger.info(
        f"Editing note title to: "
        f"{config['qa']['edit_note']['edit_title']}"
    )

    notes_page.edit_note(
        category=config["qa"]["edit_note"]["edit_category"],
        title=config["qa"]["edit_note"]["edit_title"],
        description=config["qa"]["edit_note"]["edit_description"]
    )

    sleep(5)

    all_titles = notes_page.get_all_note_titles()

    logger.info(
        f"Available note titles: {all_titles}"
    )

    assert (
        config["qa"]["edit_note"]["edit_title"]
        in all_titles
    ), "Edited note title not found"

    logger.info("Edit Note Test Passed")