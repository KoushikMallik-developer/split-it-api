import json
import uuid
from datetime import datetime
from typing import Optional
from decimal import Decimal

from pydantic import BaseModel

from users.forms import UserDetails


class ExpenseDetails(BaseModel):
    id: Optional[uuid.UUID] = None
    created_at: Optional[datetime] = None
    amount_paid: Optional[Decimal] = None
    title: Optional[str] = None
    user_paid: Optional[str] = None
    participants: Optional[str] = None
    dividing_rule: Optional[str] = None
    your_balance: Optional[Decimal] = None

    def calculate_your_balance(self, request):
        user_details = UserDetails(request).fetch()
        you_paid = Decimal(0.0)
        positive = Decimal(0.0)
        negative = Decimal(0.0)
        participants = json.loads(self.participants)
        for key, value in participants.items():
            if key == user_details.data.email:
                negative = (self.amount_paid * Decimal(value)) / 100
        if self.user_paid == user_details.data.email:
            positive = self.amount_paid
            you_paid = positive
        your_balance = positive - negative
        self.your_balance = your_balance
        return [your_balance, you_paid]
