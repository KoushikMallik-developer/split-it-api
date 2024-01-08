from typing import Optional

from pydantic import BaseModel


class RegistrationRequestType(BaseModel):
    username: str
    email: str
    fname: str
    lname: str
    password1: str
    password2: str


class RegistrationResponseType(BaseModel):
    successMessage: Optional[str] = None
    errorMessage: Optional[str] = None

    def __init__(self, **kwargs):
        if kwargs.get("errorMessage"):
            kwargs["errorMessage"] = (
                str(kwargs.get("errorMessage")).split(":")[1].strip()
            )
        super().__init__(**kwargs)
