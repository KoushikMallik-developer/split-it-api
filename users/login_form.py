import requests
from pydantic import BaseModel

from users.definitions import API_HOST, LOGIN_PATH
from users.types.login_types import LoginRequestType, LoginResponseType


class LoginForm(BaseModel):
    username: str
    password: str

    def authenticate(self, request) -> LoginResponseType:
        api_url = f"{API_HOST}{LOGIN_PATH}"
        request_data = LoginRequestType(**self.model_dump())
        response = requests.get(api_url, params=request_data.model_dump())
        response_data = LoginResponseType(**response.json())
        if response_data.token:
            request.session["is_logged_in"] = True
            request.session["access_token"] = response_data.token.get("access")
            request.session["refresh_token"] = response_data.token.get("refresh")
        else:
            request.session["is_logged_in"] = False
        return response_data
