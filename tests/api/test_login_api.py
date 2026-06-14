import pytest
from api.auth_api import AuthAPI
from config.config_reader import ConfigReader
from utils.data_reader import DataReader
from utils.logger import get_logger
logger = get_logger()

@pytest.mark.api
def test_login_api():

    logger.info("API Login Test Started")

    config = ConfigReader.read_config()
    login_data = DataReader.read_json("test_data/login_api.json")
    valid_user = (login_data["valid_user"])

    auth_api = AuthAPI(config["qa"]["api_base_url"])

    response = auth_api.login(
        valid_user["email"],
        valid_user["password"]
    )

    assert response.status_code == 200

    response_json = response.json()

    assert "data" in response_json , "Response does not contain 'data' key"

    token = (response_json["data"]["token"])

    assert token is not None , "Authentication token is missing"

    assert len(token) > 0 , "Authentication token is empty"

    logger.info("API Login Test Passed")