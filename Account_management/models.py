from django.db import models
from django.contrib.auth.models import AbstractUser
from Character_Menagement.models import Character


# User-Character one-to-many relation
#class User(AbstractUser):
#    Characters = models.ForeignKey()