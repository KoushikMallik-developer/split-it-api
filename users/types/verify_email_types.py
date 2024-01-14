from typing import Optional

from pydantic import BaseModel

from users.types.base_response_type import BaseResponseType


class VerifyEmailRequestType(BaseModel):
    email: str
    otp: str


class VerifyEmailResponseType(BaseResponseType):
    token: Optional[dict] = None
