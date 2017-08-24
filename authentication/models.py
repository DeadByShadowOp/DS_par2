from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# AbstractUser already has the following fields and others.
# username, first_name, last_name
# email, password, groups


class customuser(AbstractUser):
    matricula = models.CharField(max_length=9, null=True)

    def is_Student(self):
      return self.matricula is not None
    # to enforce that you require email field to be associated with
    # every user at registration
    REQUIRED_FIELDS = ["email"]