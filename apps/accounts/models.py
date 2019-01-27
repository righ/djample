import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
