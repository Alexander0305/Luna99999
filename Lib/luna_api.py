# luna_api.py

import requests

class LunaAPI:
    def init(self):
        self.base_url = "https://api.luna.ai"

    def get_data(self, endpoint):
        # Get data from Luna API
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json()
