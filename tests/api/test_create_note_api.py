import pytest

from utils.data_reader import DataReader


@pytest.mark.api
def test_create_note_api(api_client):

    data = DataReader.read_json(
        "test_data/create_note.json"
    )

    note = data["valid_note"]

    response = (
        api_client["notes_api"].create_note(
            category=note["category"],
            title=note["title"],
            description=note["description"],
            token=api_client["token"]
        )
    )

    assert response.status_code == 200

    response_data = response.json()["data"]

    assert response_data["title"] == note["title"]

    assert response_data["description"]==note["description"]

    assert response_data["category"] == note["category"]
