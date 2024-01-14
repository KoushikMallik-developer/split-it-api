from django.urls import path
from .views import expense_list, create_expense

urlpatterns = [
    path("expenses/", expense_list, name="expense-list"),
    path("create-expense/<str:id>/", create_expense, name="create-expense"),
]
