import os
from datetime import datetime
import pytest
from selenium.webdriver.support.ui import Select
from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.data_reader import DataReader
from utils.logger import get_logger
logger = get_logger()


@pytest.mark.ui
@pytest.mark.parametrize("scenario",["missing_title","missing_description", "all_fields_empty"])

def test_invalid_create_note_ui(browser,scenario):

    logger.info(f"Invalid Create Note Test Started - {scenario}")

    config = ConfigReader.read_config()
    data = DataReader.read_json("test_data/create_note.json")
    note = data[scenario]

    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("Logging into application")

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    notes_page.scroll_by_offset()

    notes_page.click(notes_page.ADD_NOTE)

    if note["category"]:
        dropdown = notes_page.wait.until(
            lambda d: d.find_element(*notes_page.CATEGORY)
        )
        Select(dropdown).select_by_visible_text(note["category"])

    if note["title"]:
        notes_page.type(notes_page.TITLE,note["title"])

    if note["description"]:
        notes_page.type(notes_page.DESCRIPTION,note["description"])

    notes_page.click(notes_page.SAVE_BTN)

    logger.info(f"Capturing screenshot for {scenario}")

    os.makedirs("reports/screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = (f"reports/screenshots/"f"invalid_create_note_{scenario}_{timestamp}.png")
    browser.save_screenshot(screenshot_path)

    assert "notes/app" in browser.current_url

    logger.info(f"Invalid Create Note Test Passed - {scenario}")