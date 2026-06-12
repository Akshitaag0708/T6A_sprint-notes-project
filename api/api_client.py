import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, headers=None):
        return self.session.get(url=f"{self.base_url}{endpoint}",headers=headers)

    def post(self, endpoint, payload=None, headers=None):
        return self.session.post(url=f"{self.base_url}{endpoint}",json=payload,headers=headers)

    def put(self, endpoint, payload=None, headers=None):
        return self.session.put(url=f"{self.base_url}{endpoint}",json=payload,headers=headers)

    def delete(self, endpoint, headers=None):
        return self.session.delete(url=f"{self.base_url}{endpoint}",headers=headers)