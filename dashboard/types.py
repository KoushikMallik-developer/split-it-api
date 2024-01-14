import json
import uuid
from typing import Optional

from pydantic import BaseModel


class ExportGroupDetails(BaseModel):
    id: Optional[uuid.UUID] = None
    name: Optional[str] = None
    members: Optional[list] = None

    def __init__(self, **kwargs):
        if kwargs.get("members"):
            kwargs["members"] = json.loads(kwargs.get("members"))
        super().__init__(**kwargs)
