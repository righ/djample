import hashlib
import uuid

from django.utils.http import urlencode
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(unique=True)
    file = models.FileField(null=True, upload_to='userfiles/')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f'{self.name} (ID:{self.id})'

    def gravatar(self, querystring):
        md5 = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{md5}?{querystring}'


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    users = models.ManyToManyField(User, related_name='belongs')
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='mygroups')
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, related_name='children')

    def __str__(self):
        return f'{self.name} (ID:{self.id})'
