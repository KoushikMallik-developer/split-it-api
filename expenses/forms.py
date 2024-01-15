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
    dividing_rule: Optional[str] = None

    def __init__(self, **kwargs):
        amount = kwargs.get("amount_paid")
        if amount:
            if not isinstance(amount, Decimal):
                kwargs["amount"] = Decimal(amount)

        participants = kwargs.get("participants")
        if isinstance(participants, list) and len(participants) > 0:
            if kwargs.get("dividing_rule") and isinstance(
                kwargs.get("dividing_rule"), str
            ):
                kwargs["dividing_rule"] = str(kwargs.get("dividing_rule")).upper()
                if kwargs.get("dividing_rule") == "EQUALLY":
                    participant_count = len(participants)
                    each_percentage = 100 / participant_count
                    participants = {
                        participant: each_percentage for participant in participants
                    }
            kwargs["participants"] = json.dumps(participants)
        super().__init__(**kwargs)

    def create_expense(self, group_id):
        if self.amount_paid and self.title and self.user_paid and self.participants:
            expense = Expense(**self.model_dump())
            expense.group = ExpenseGroup.objects.get(id=group_id)
            expense.save()
            return {"successMessage": "Expense added successfully."}
        return {"errorMessage": "Invalid input provided."}
