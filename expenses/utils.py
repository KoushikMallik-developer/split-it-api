from .models import Expense
from django.db.models import Sum


def calculate_total_expenses(user):
    total_expenses = Expense.objects.filter(user_paid=user).aggregate(
        models.Sum("amount")
    )
    return total_expenses["amount__sum"] or 0


def settle_debts(user):
    user_expenses = Expense.objects.filter(user_paid=user)
    total_spent = user_expenses.aggregate(Sum("amount"))["amount__sum"] or 0

    # Calculate debts
    debts = {}
    for expense in user_expenses:
        participants = expense.participants.all()
        share = expense.amount / (
            participants.count() + 1
        )  # Including the user who paid
        for participant in participants:
            if participant != user:
                debts[participant] = debts.get(participant, 0) + share

    # Find users owed money and users owing money
    users_owed = {k: v - total_spent for k, v in debts.items() if v > total_spent}
    users_owing = {k: total_spent - v for k, v in debts.items() if v <= total_spent}

    return users_owed, users_owing
