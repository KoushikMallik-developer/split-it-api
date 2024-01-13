import logging
import uuid

from django.core.exceptions import FieldError
from django.db import models  # Use the custom user model from the 'users' app


class ExpenseGroup(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, null=False, editable=False
    )
    name = models.CharField(max_length=255)
    members = models.CharField(max_length=20000)

    def __str__(self):
        return self.name

    def model_to_dict(self) -> dict:
        try:
            return {
                field.name: getattr(self, field.name) for field in self._meta.fields
            }
        except Exception:
            logging.error("Error occured  while converting model to dict")
            raise FieldError("Error occured  while converting model to dict")
