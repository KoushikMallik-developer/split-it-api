from pydantic import BaseModel

from users.types.base_response_type import BaseResponseType


class ResendOTPRequestType(BaseModel):
    email: str


class ResendOTPResponseType(BaseResponseType):
    pass
