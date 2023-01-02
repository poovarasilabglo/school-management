from django.urls import path,include
from apps.student.views import StudentRegisterAPIView

urlpatterns = [
    path('student/',StudentRegisterAPIView.as_view()),
]