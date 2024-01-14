import json

import requests

from users.definitions import API_HOST, USER_DETAILS_PATH
from users.types.user_details_types import UserDetailsResponseType


class UserDetails:
    def __init__(self, request):
        self.request = request

    def fetch(self):
        if self.request.session.get("user_details"):
            return UserDetailsResponseType(
                **json.loads(self.request.session.get("user_details"))
            )
        api_url = f"{API_HOST}{USER_DETAILS_PATH}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.request.session.get('access_token')}",
        }
        response = requests.get(api_url, headers=headers)
        response_data = UserDetailsResponseType(**response.json())
        self.request.session["user_details"] = response_data.model_dump_json()
        return response_data
