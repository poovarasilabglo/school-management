from django.shortcuts import render
from rest_framework import generics
from apps.student.models import Student
from apps.student.serializers import StudentRegisterSerializers
#from rest_framework.permissions import AllowAny
from apps.user.permissions import IsTeacherOrIsStudent


class StudentRegisterAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    permission_classes = (IsTeacherOrIsStudent,)
    serializer_class = StudentRegisterSerializers

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user= user)



