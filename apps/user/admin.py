from django.contrib import admin
from apps.user.models import User


class Useradmin(admin.ModelAdmin):
    list_display = ('id','is_staff','is_accountant','is_teacher','is_student','is_parent')
admin.site.register(User,Useradmin)

