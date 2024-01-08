from typing import Optional

from pydantic import BaseModel


class LoginRequestType(BaseModel):
    email: str
    password: str


class LoginResponseType(BaseModel):
    token: Optional[dict]
    errorMessage: Optional[str]
