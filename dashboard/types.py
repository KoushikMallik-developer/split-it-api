import json
import uuid
from typing import Optional, List

from decimal import Decimal
from pydantic import BaseModel

from expenses.utils import ExpenseDetails


class ExportGroupDetails(BaseModel):
    id: Optional[uuid.UUID] = None
    name: Optional[str] = None
    members: Optional[list] = None
    expenses: Optional[List[ExpenseDetails]] = None
    total_balance: Optional[Decimal] = None
    you_paid: Optional[Decimal] = None
    your_balance: Optional[Decimal] = None

    def __init__(self, **kwargs):
        if kwargs.get("members"):
            kwargs["members"] = json.loads(kwargs.get("members"))

        super().__init__(**kwargs)
