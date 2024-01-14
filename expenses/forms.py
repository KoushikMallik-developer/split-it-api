import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from dashboard.models import ExpenseGroup
from expenses.models import Expense


class ExpenseForm(BaseModel):
    amount_paid: Optional[Decimal] = None
    title: Optional[str] = None
    user_paid: Optional[str] = None
    participants: Optional[str] = None

    def __init__(self, **kwargs):
        participants = []
        key = "participant"
        count = 1
        while True:
            current_key = key + str(count)
            if kwargs.get(current_key):
                if kwargs.get(current_key) != "":
                    participants.append(kwargs.get(current_key))
                    count += 1
            else:
                break
        if len(participants) > 0:
            kwargs["participants"] = json.loads(participants)
        super().__init__(**kwargs)

    def create_expense(self, group_id):
        if self.amount_paid and self.title and self.user_paid and self.participants:
            expense = Expense(**self.model_dump())
            expense.group = ExpenseGroup.objects.get(id=group_id)
            expense.save()
            return {"successMessage": "Expense added successfully."}
        return {"errorMessage": "Invalid input provided."}
