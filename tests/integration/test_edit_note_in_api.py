import pytest
from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.data_reader import DataReader
from utils.logger import get_logger
logger = get_logger()


@pytest.mark.integration
def test_edit_note_ui_api( browser, api_client):

    logger.info("Integration Test Started - UI Edit to API Validate" )

    config = ConfigReader.read_config()
    create_data = DataReader.read_json("test_data/create_note.json")
    edit_data = DataReader.read_json("test_data/edit_note.json")

    create_note = create_data["integration_edit_note"]
    edit_note = edit_data["integration_edit"]

    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("Logging into application via ui")
    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    logger.info("Creating note via ui")
    notes_page.create_note(
        category=create_note["category"],
        title=create_note["title"],
        description=create_note["description"]
    )

    logger.info("Editing note via ui")
    notes_page.edit_note(
        category=edit_note["category"],
        title=edit_note["title"],
        description=edit_note["description"]
    )

    logger.info("getting all notes via api")
    response = (
        api_client["notes_api"]
        .get_all_notes(
            api_client["token"]
        )
    )

    assert response.status_code == 200

    notes = response.json()["data"]

    matched_note = None

    for note in notes:

        if (note["title"] == edit_note["title"]
            and note["description"]  == edit_note["description"]
            and note["category"]  == edit_note["category"]):

            matched_note = note
            break


    assert matched_note is not None, (
            "Edited note not found in API response"
        )

    assert  matched_note["title"]  ==  edit_note["title"]


    assert  matched_note["description"] == edit_note["description"]


    assert  matched_note["category"] ==  edit_note["category"]

    logger.info(
        "Integration Test Passed"
    )