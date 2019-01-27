from django.db import models
from django.utils import timezone

# Create your models here.


class Status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=10)
    description = models.TextField()


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)

    user = models.ForeignKey('accounts.User', null=True)
    group = models.ForeignKey('accounts.Group', null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Time(models.Model):
    id = models.BigAutoField(primary_key=True)
    note = models.TextField(default='')
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)


class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.ForeignKey('accounts.User')
    status = models.ForeignKey(Status)
    content = models.TextField(default='')

    tags = models.ManyToManyField(Tag)
    times = models.ManyToManyField(Time)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

