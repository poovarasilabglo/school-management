from django.urls import path
from apps.teacher.views import TeacherRegisterAPIView

urlpatterns = [
    path('teacher/',TeacherRegisterAPIView.as_view()),
]