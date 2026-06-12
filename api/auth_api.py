from api.api_client import APIClient


class AuthAPI(APIClient):

    LOGIN_ENDPOINT = "/users/login"

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        return self.post(
            endpoint=self.LOGIN_ENDPOINT,
            payload=payload
        )