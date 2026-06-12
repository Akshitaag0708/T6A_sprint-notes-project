import pytest

from api.auth_api import AuthAPI
from api.notes_api import NotesAPI
from config.config_reader import ConfigReader


@pytest.fixture(scope="function")
def api_client():

    config = ConfigReader.read_config()["qa"]

    auth_api = AuthAPI(config["api_base_url"])

    login_response = auth_api.login(
        config["email"],
        config["password"]
    )

    assert login_response.status_code == 200, "API Login Failed"

    token = login_response.json()["data"]["token"]

    return {
        "token": token,
        "notes_api": NotesAPI(config["api_base_url"])
    }