from django.contrib import admin
from apps.teacher.models import Teacher


class Teacheradmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'teacher_id',
                    'name',
                    'image',
                    'dob',
                    'gender',
                    'phone',
                    'address',
                    'join_year')
admin.site.register(Teacher,Teacheradmin)



