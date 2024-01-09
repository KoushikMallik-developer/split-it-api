from typing import Optional

from pydantic import BaseModel

from users.types.base_response_type import BaseResponseType


class LoginRequestType(BaseModel):
    email: str
    password: str


class LoginResponseType(BaseResponseType):
    token: Optional[dict] = None
