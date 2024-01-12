from django.db import models
from dashboard.models import ExpenseGroup


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    user_paid = models.CharField(max_length=2000)
    participants = models.CharField(max_length=20000, null=True)
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
