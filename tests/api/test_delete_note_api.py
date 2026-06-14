import pytest
from utils.data_reader import DataReader
from utils.logger import get_logger
logger = get_logger()


@pytest.mark.api
def test_delete_note_api(api_client):

    logger.info("Deleting note via api test started")

    data = DataReader.read_json("test_data/create_note.json")
    note = data["valid_note"]

    logger.info("Creating note via api")

    create_response = (
        api_client["notes_api"].create_note(
            category=note["category"],
            title=note["title"],
            description=note["description"],
            token=api_client["token"]
        )
    )

    assert create_response.status_code == 200

    note_id = (create_response.json()["data"]["id"])

    logger.info("Deleting note via api")
    delete_response = (
        api_client["notes_api"].delete_note(
            note_id=note_id,
            token=api_client["token"]
        )
    )

    assert delete_response.status_code == 200

    logger.info("Deleting note via api test passed")