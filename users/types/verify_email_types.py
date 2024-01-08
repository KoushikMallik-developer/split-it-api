from typing import Optional

from pydantic import BaseModel


class VerifyEmailRequestType(BaseModel):
    email: str
    otp: str


class VerifyEmailResponseType(BaseModel):
    token: Optional[dict]
    errorMessage: Optional[str]
