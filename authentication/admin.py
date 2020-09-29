from django.contrib import admin

# Register your models here.
from authentication.models import (
    User, UserProfile
    # UserDevices
)
from django.contrib.auth.models import Group


admin.site.unregister(Group)

admin.site.register(User)
# admin.site.register(BlackList)
admin.site.register(UserProfile)
# admin.site.register(UserDevices)

