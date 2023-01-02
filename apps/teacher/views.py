from django.shortcuts import render
from rest_framework import generics
from apps.teacher.models import Teacher
from apps.teacher.serializers import TeacherRegisterSerializers
from rest_framework.permissions import AllowAny
from apps.user.permissions import IsTeacher



class TeacherRegisterAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    permission_classes = (IsTeacher,)
    serializer_class = TeacherRegisterSerializers

    def get_queryset(self):
        user = self.request.user
        return Teacher.objects.filter(user= user)




