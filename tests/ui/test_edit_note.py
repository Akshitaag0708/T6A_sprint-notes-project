import pytest
from time import sleep
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from config.config_reader import ConfigReader
from utils.logger import get_logger
logger = get_logger()


@pytest.mark.ui
def test_edit_note(browser):

    logger.info("Edit Note Test Started")

    config = ConfigReader.read_config()
    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("logging into application")

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    logger.info(f"Creating note with title: {config['qa']['ui_create_note']['ui_title']}")
    notes_page.create_note(
        category=config["qa"]["ui_create_note"]["ui_category"],
        title=config["qa"]["ui_create_note"]["ui_title"],
        description=config["qa"]["ui_create_note"]["ui_description"]
    )

    logger.info("Test note created successfully")

    logger.info("Editing newly created note")
    notes_page.edit_note(
        category=config["qa"]["ui_edit_note"]["ui_edit_category"],
        title=config["qa"]["ui_edit_note"]["ui_edit_title"],
        description=config["qa"]["ui_edit_note"]["ui_edit_description"]
    )

    sleep(3)

    all_titles = notes_page.get_all_note_titles()


    assert config["qa"]["ui_edit_note"]["ui_edit_title"] in all_titles, "Edited note title not found"

    logger.info("Edit Note Test Passed")