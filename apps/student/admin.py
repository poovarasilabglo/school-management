from django.contrib import admin
from apps.student.models import Student,Subject


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
                    'session_year',
                    'teacher')
admin.site.register(Student,Studentadmin)


class Subjectadmin(admin.ModelAdmin):
    list_display = ('id',
                    'teacher',
                    'student',
                    'subject_code',
                    'subject_name',
                    'subject_mark',
                   )
admin.site.register(Subject,Subjectadmin)
