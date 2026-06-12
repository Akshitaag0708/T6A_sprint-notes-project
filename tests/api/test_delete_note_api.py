import pytest

from utils.data_reader import DataReader


@pytest.mark.api
def test_delete_note_api(api_client):

    data = DataReader.read_json(
        "test_data/create_note.json"
    )

    note = data["valid_note"]

    create_response = (
        api_client["notes_api"].create_note(
            category=note["category"],
            title=note["title"],
            description=note["description"],
            token=api_client["token"]
        )
    )

    note_id = (
        create_response
        .json()["data"]["id"]
    )

    delete_response = (
        api_client["notes_api"].delete_note(
            note_id=note_id,
            token=api_client["token"]
        )
    )

    assert delete_response.status_code == 200