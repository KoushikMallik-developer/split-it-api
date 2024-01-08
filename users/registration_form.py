import logging
from typing import Optional

from pydantic import BaseModel
import requests

from users.definitions import API_HOST, REGISTRATION_PATH, VERIFY_EMAIL_PATH
from users.types.registration_types import (
    RegistrationRequestType,
    RegistrationResponseType,
)
from users.types.verify_email_types import (
    VerifyEmailRequestType,
    VerifyEmailResponseType,
)


class RegistrationForm(BaseModel):
    username: Optional[str] = None
    email: str
    fname: str
    lname: str
    password1: str
    password2: str

    def register(self, request) -> RegistrationResponseType:
        api_url = f"{API_HOST}{REGISTRATION_PATH}"
        request_data = RegistrationRequestType(**self.model_dump())
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            api_url, data=request_data.model_dump_json(), headers=headers
        )
        response_data = RegistrationResponseType(**response.json())
        # if response_data.successMessage:
        #     request.session["is_logged_in"] = True
        return response_data


class VerifyEmailForm(BaseModel):
    email: str
    otp: str

    def verify(self, request):
        api_url = f"{API_HOST}{VERIFY_EMAIL_PATH}"
        request_data = VerifyEmailRequestType(**self.model_dump())
        response = requests.get(api_url, params=request_data.model_dump())
        response_data = VerifyEmailResponseType(**response.json())
        if response_data.token:
            request.session["is_logged_in"] = True
            request.session["access_token"] = response_data.token.get("access")
            request.session["refresh_token"] = response_data.token.get("refresh")
        else:
            request.session["is_logged_in"] = False
        return response_data
