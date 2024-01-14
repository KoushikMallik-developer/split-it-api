from typing import Optional

from pydantic import BaseModel

from users.types.base_response_type import BaseResponseType


class UserDetailType(BaseModel):
    id: Optional[str]
    username: Optional[str]
    email: Optional[str]
    fname: Optional[str]
    lname: Optional[str]
    dob: Optional[str]
    phone: Optional[str]
    image: Optional[str]
    is_active: Optional[bool]
    account_type: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]


class UserDetailsResponseType(BaseResponseType):
    data: Optional[UserDetailType]
