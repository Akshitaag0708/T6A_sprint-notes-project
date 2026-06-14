import pytest
import time
from utils.logger import get_logger
logger = get_logger()

@pytest.mark.api
def test_get_all_notes(api_client):

    logger.info("Testing get_all_notes")

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    start_time = time.time()

    response = notes_api.get_all_notes( token)

    response_time = ( time.time() - start_time)


    assert response.status_code == 200

    response_json = response.json()

    assert "data" in response_json

    assert isinstance(response_json["data"], list)


    assert response_time < 2, (
        f"Response time exceeded: "
        f"{response_time:.2f} sec")

    logger.info("Getting all notes via api test passed")