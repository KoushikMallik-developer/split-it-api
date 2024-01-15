from django.shortcuts import render, redirect

from dashboard.utils import GroupUtils
from .forms import ExpenseForm
from .models import Expense


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, "expenses/expense_list.html", {"expenses": expenses})


def create_expense(request, id):
    id = id.split("=")[1]
    context = {"is_logged_in": request.session.get("is_logged_in")}
    group = GroupUtils().get_group_details(request, id)
    context.update(group.model_dump())
    if request.method == "POST":
        post_dict = request.POST.dict()
        post_dict["participants"] = request.POST.getlist("participants")
        response = ExpenseForm(**post_dict).create_expense(group_id=id)
        context.update(response)
        if response.get("successMessage"):
            return redirect(f"/groups/id={id}")
        else:
            return render(request, "expenses/create_expense.html", context)
    else:
        return render(request, "expenses/create_expense.html", context)
