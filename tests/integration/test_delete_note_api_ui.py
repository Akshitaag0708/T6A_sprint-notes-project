import pytest

from config.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from utils.data_reader import DataReader
from utils.logger import get_logger

logger = get_logger()

@pytest.mark.integration
def test_delete_note_api_ui(
        browser,
        api_client
):
    logger.info(
        "Integration Test Started - API Delete → UI Validate"
    )

    config = ConfigReader.read_config()

    data = DataReader.read_json(
        "test_data/create_note.json"
    )

    note = data["integration_delete_note"]

    # Create Note via API
    create_response = (
        api_client["notes_api"].create_note(
            category=note["category"],
            title=note["title"],
            description=note["description"],
            token=api_client["token"]
        )
    )

    assert create_response.status_code == 200

    note_id = (
        create_response
        .json()["data"]["id"]
    )

    # Delete Note via API
    delete_response = (
        api_client["notes_api"].delete_note(
            note_id=note_id,
            token=api_client["token"]
        )
    )

    assert delete_response.status_code == 200

    # Login UI
    login_page = LoginPage(browser)
    notes_page = NotesPage(browser)

    login_page.login(
        config["qa"]["email"],
        config["qa"]["password"]
    )

    # Refresh UI
    notes_page.refresh_page()

    # Get all visible note titles
    all_titles = (notes_page.get_all_note_titles())

    # Validate note is missing
    assert (note["title"] not in all_titles), (
        f"Deleted note "
        f"'{note['title']}' "
        f"is still visible in UI"
    )

    logger.info(
        "Integration Test Passed"
    )