from typing import Optional

from pydantic import BaseModel


class BaseResponseType(BaseModel):
    errorName: Optional[str] = None
    successMessage: Optional[str] = None
    errorMessage: Optional[str] = None

    def __init__(self, **kwargs):
        if kwargs.get("errorMessage"):
            kwargs["errorName"] = str(kwargs.get("errorMessage")).split(":")[0].strip()
            kwargs["errorMessage"] = (
                str(kwargs.get("errorMessage")).split(":")[1].strip()
            )
        super().__init__(**kwargs)
