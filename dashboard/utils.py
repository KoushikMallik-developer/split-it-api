from decimal import Decimal

from dashboard.models import ExpenseGroup
from dashboard.types import ExportGroupDetails
from expenses.models import Expense
from expenses.utils import ExpenseDetails


class GroupUtils:
    @staticmethod
    def get_group_details(request, group_id):
        if group_id:
            if ExpenseGroup.objects.filter(id=group_id).exists():
                group = ExpenseGroup.objects.get(id=group_id)
                expenses = Expense.objects.filter(group__id=group_id)
                export_expenses = []
                total_balance = Decimal(0.0)
                you_paid = Decimal(0.0)
                your_balance = Decimal(0.0)
                for expense in expenses:
                    temp_expense = ExpenseDetails(**expense.model_to_dict())
                    _, temp_you_paid = temp_expense.calculate_your_balance(request)
                    export_expenses.append(temp_expense)
                    total_balance += temp_expense.amount_paid
                    your_balance += temp_expense.your_balance
                    you_paid += temp_you_paid
                group = ExportGroupDetails(**group.model_to_dict())
                group.expenses = export_expenses
                group.your_balance = your_balance
                group.you_paid = you_paid
                group.total_balance = total_balance
                return group
