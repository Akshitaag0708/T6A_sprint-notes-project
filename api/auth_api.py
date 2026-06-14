from api.api_client import APIClient
import allure

class AuthAPI(APIClient):

    login_endpoint = "/users/login"

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        response = self.post(endpoint=self.login_endpoint,payload=payload)

        allure.attach(
            response.text,
            name="Login Response",
            attachment_type=allure.attachment_type.JSON
        )

        return response