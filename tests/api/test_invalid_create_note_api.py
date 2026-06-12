import pytest

from utils.data_reader import DataReader


@pytest.mark.api
@pytest.mark.parametrize(
    "scenario",
    [
        "missing_title",
        "missing_description",
        "all_fields_empty"
    ]
)
def test_invalid_create_note_api(
        api_client,
        scenario
):

    data = DataReader.read_json(
        "test_data/create_note.json"
    )

    note = data[scenario]

    response = (
        api_client["notes_api"].create_note(
            category=note["category"],
            title=note["title"],
            description=note["description"],
            token=api_client["token"]
        )
    )

    assert response.status_code == 400