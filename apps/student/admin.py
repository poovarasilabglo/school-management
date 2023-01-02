from django.contrib import admin
from apps.student.models import Student


class Studentadmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'name',
                    'student_id',
                    'profile_picture',
                    'dob',
                    'gender',
                    'father_name',
                    'mother_name',
                    'phone',
                    'address',
                    'std',
                    'session_year')
admin.site.register(Student,Studentadmin)
