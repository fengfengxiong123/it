from django.contrib import admin
from share.models import Dot
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Dot)


# admin.site.unregister(User)


class UserDotInline(admin.StackedInline):
    model = Dot


class UserProfileotAdmin(UserAdmin):
    inlines = [UserDotInline, ]


admin.site.register(User, UserProfileotAdmin)
