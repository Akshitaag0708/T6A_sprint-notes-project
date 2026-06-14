from api.api_client import APIClient
import allure

class NotesAPI(APIClient):

    notes_endpoint = "/notes"

    def get_all_notes(self, token):
        headers = {"x-auth-token": token}
        response = self.get(endpoint=self.notes_endpoint,headers=headers)

        allure.attach(response.text, name="Get All Notes Response", attachment_type=allure.attachment_type.JSON)

        return response
        # return self.get(endpoint=self.notes_endpoint,headers=headers)

    def create_note(self,category,title,description,token):

        headers = {"x-auth-token": token}
        payload = {
            "category": category,
            "title": title,
            "description": description
        }
        response = self.post(endpoint=self.notes_endpoint,payload=payload,headers=headers)
        allure.attach( response.text, name="Create Note Response", attachment_type=allure.attachment_type.JSON)

        return response

        # return self.post(endpoint=self.notes_endpoint,payload=payload,headers=headers)

    def update_note(self,note_id,category,title,description,completed,token):

        headers = {"x-auth-token": token}
        payload = {
            "category": category,
            "title": title,
            "description": description,
            "completed": completed
        }
        response = self.put(endpoint=f"{self.notes_endpoint}/{note_id}",payload=payload,headers=headers)

        allure.attach(response.text, name="Update Note Response", attachment_type=allure.attachment_type.JSON)

        return response
        # return self.put(endpoint=f"{self.notes_endpoint}/{note_id}",payload=payload,headers=headers)

    def delete_note(self, note_id, token):

        headers = {"x-auth-token": token}
        response = self.delete(endpoint=f"{self.notes_endpoint}/{note_id}", headers=headers)

        allure.attach( response.text,  name="Delete Note Response", attachment_type=allure.attachment_type.JSON)

        return response

        # return self.delete(endpoint=f"{self.notes_endpoint}/{note_id}",headers=headers)