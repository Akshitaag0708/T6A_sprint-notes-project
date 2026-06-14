import pytest
from utils.data_reader import DataReader
from utils.logger import get_logger
logger = get_logger()

@pytest.mark.api
def test_create_note_api(api_client):

    logger.info("Creating note via api test started")

    data = DataReader.read_json("test_data/create_note.json")
    note = data["valid_note"]

    logger.info("Creating note via api ")

    response = (
        api_client["notes_api"].create_note(
            category = note["category"],
            title = note["title"],
            description = note["description"],
            token = api_client["token"]
        )
    )

    assert response.status_code == 200

    response_data = response.json()["data"]

    assert response_data["title"] == note["title"]

    assert response_data["description"] == note["description"]

    assert response_data["category"] == note["category"]

    logger.info("Finished creating note via api test")
