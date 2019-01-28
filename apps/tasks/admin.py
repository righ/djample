from django import forms
from django.contrib import admin

from .models import Status


# Now register the new UserAdmin...
admin.site.register(Status)

