from django.db import models  # Use the custom user model from the 'users' app


class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.CharField(max_length=20000)

    def __str__(self):
        return self.name
