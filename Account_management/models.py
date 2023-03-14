from django.db import models
from django.contrib.auth.models import AbstractUser
from Character_Menagement.models import Character


# User-Character one-to-many relation
class L5RUser(AbstractUser):
    characters = models.ForeignKey(Character, null=True, on_delete=models.SET_NULL)
