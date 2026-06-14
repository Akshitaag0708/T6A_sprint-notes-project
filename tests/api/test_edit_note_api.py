import pytest
from utils.data_reader import DataReader
from utils.logger import get_logger
logger = get_logger()

@pytest.mark.api
def test_edit_note_api(api_client):

    logger.info("Editing note via api test Started")

    create_data = DataReader.read_json( "test_data/create_note.json")
    edit_data = DataReader.read_json("test_data/edit_note.json")
    create_note = create_data["valid_note"]
    edit_note = edit_data["valid_edit"]

    logger.info("Creating note via api")

    create_response = (
        api_client["notes_api"].create_note(
            category=create_note["category"],
            title=create_note["title"],
            description=create_note["description"],
            token=api_client["token"]
        )
    )

    note_id = (create_response.json()["data"]["id"])

    logger.info("Editing note via api")

    update_response = (
        api_client["notes_api"].update_note(
            note_id=note_id,
            category=edit_note["category"],
            title=edit_note["title"],
            description=edit_note["description"],
            completed=edit_note["completed"],
            token=api_client["token"]
        )
    )

    assert update_response.status_code == 200

    response_data = (update_response.json()["data"])

    assert response_data["title"]  == edit_note["title"]

    assert response_data["description"] == edit_note["description"]

    assert response_data["category"] == edit_note["category"]

    assert response_data["completed"] == edit_note["completed"]

    logger.info("Editing note via api test passed")