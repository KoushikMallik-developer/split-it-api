from django.db import models
from users.models import User  # Use the custom user model from the 'users' app

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name
