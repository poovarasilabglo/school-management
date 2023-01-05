from django.urls import path,include
from apps.student.views import StudentRegisterViewSet,StudentListView,SubjectViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'student',StudentRegisterViewSet),
router.register(r'list',StudentListView),
router.register(r'subject', SubjectViewSet),


urlpatterns = [
    path('',include(router.urls)),
]