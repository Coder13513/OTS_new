from django.contrib import admin

# Register your models here.
from authentication.models import (
    User,)
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(User)

