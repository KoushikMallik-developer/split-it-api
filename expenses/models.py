import logging
import uuid

from django.core.exceptions import FieldError
from django.db import models
from dashboard.models import ExpenseGroup


class Expense(models.Model):
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.TextField()
    user_paid = models.CharField(max_length=2000)
    participants = models.CharField(max_length=20000, null=True)
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    dividing_rule = models.CharField(max_length=20)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, null=False, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def model_to_dict(self) -> dict:
        try:
            return {
                field.name: getattr(self, field.name) for field in self._meta.fields
            }
        except Exception:
            logging.error("Error occured  while converting model to dict")
            raise FieldError("Error occured  while converting model to dict")

    def __str__(self):
        return self.title
