from pydantic import BaseModel

from users.types.base_response_type import BaseResponseType


class RegistrationRequestType(BaseModel):
    username: str
    email: str
    fname: str
    lname: str
    password1: str
    password2: str


class RegistrationResponseType(BaseResponseType):
    pass
