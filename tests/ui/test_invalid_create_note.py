import pytest
import os
from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.data_reader import DataReader
from utils.logger import get_logger

logger = get_logger()


@pytest.mark.ui
@pytest.mark.parametrize(
    "scenario",
    [
        "missing_title",
        "missing_description",
        "all_fields_empty"
    ]
)
def test_invalid_create_note_ui(
        browser,
        scenario
):

    logger.info(
        f"Invalid Create Note Test Started - {scenario}"
    )

    config = ConfigReader.read_config()

    browser.get(
        config["qa"]["base_url"]
    )

    data = DataReader.read_json(
        "test_data/create_note.json"
    )

    note = data[scenario]

    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("Logging into application")

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    notes_page.scroll_by_offset()

    notes_page.click(
        notes_page.ADD_NOTE
    )

    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    screenshot_path = (
        f"screenshots/"
        f"invalid_create_note_{scenario}.png"
    )

    browser.save_screenshot(
        screenshot_path
    )

    logger.info(
        f"Screenshot saved: {screenshot_path}"
    )





    logger.info(
        f"Executing scenario: {scenario}"
    )

    # Category
    if note["category"]:

        from selenium.webdriver.support.ui import Select

        dropdown = notes_page.wait.until(
            lambda d: d.find_element(
                *notes_page.CATEGORY
            )
        )

        Select(dropdown).select_by_visible_text(
            note["category"]
        )

    # Title
    if note["title"]:
        notes_page.type(
            notes_page.TITLE,
            note["title"]
        )

    # Description
    if note["description"]:
        notes_page.type(
            notes_page.DESCRIPTION,
            note["description"]
        )

    notes_page.click(
        notes_page.SAVE_BTN
    )

    logger.info(
        f"Current URL: {browser.current_url}"
    )

    assert "notes/app" in browser.current_url

    logger.info(
        f"Invalid Create Note Test Passed - {scenario}"
    )