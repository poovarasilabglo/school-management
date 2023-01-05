from django.urls import path,include
from apps.teacher.views import TeacherRegisterViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'teacher', TeacherRegisterViewSet),


urlpatterns = [
     path('',include(router.urls)),
]