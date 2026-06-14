import pytest

from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.data_reader import DataReader
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.integration
def test_validate_note_exists_in_api(browser, api_client):

    logger.info("Integration Test Started - UI Create to API Validate" )

    config = ConfigReader.read_config()
    data = DataReader.read_json("test_data/create_note.json")
    note = data["integration_note"]

    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    logger.info("Logging into application via ui")

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    logger.info("Creating a note via ui")

    notes_page.create_note(
        category=note["category"],
        title=note["title"],
        description=note["description"]
    )

    logger.info("Getting all notes via api")

    response = (
        api_client["notes_api"]
        .get_all_notes(
            api_client["token"]
        )
    )

    assert response.status_code == 200

    notes = response.json()["data"]

    matched_note = None

    for api_note in notes:

        if (api_note["title"] == note["title"] and api_note["description"] == note["description"]):
            matched_note = api_note
            break

    assert matched_note is not None, (
        "Created note not found in API response"
    )

    assert  matched_note["title"] == note["title"]

    assert  matched_note["description"] == note["description"]

    assert  matched_note["category"] == note["category"]

    logger.info( "Integration Test Passed")
