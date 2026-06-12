import pytest

from api.auth_api import AuthAPI
from config.config_reader import ConfigReader
from utils.data_reader import DataReader


@pytest.mark.api
@pytest.mark.parametrize(
    "user_type",
    [
        "invalid_email",
        "invalid_password"
    ]
)
def test_invalid_login_api(user_type):

    config = ConfigReader.read_config()

    login_data = DataReader.read_json(
        "test_data/login_api.json"
    )

    user = login_data[user_type]

    auth_api = AuthAPI(
        config["qa"]["api_base_url"]
    )

    response = auth_api.login(
        user["email"],
        user["password"]
    )

    assert response.status_code == 401