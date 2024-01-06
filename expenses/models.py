from django.db import models
from users.models import User
from dashboard.models import Group

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    user_paid = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participants')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
