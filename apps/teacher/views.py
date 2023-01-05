from apps.teacher.models import Teacher
from apps.teacher.serializers import TeacherRegisterSerializers
from apps.user.permissions import IsTeacher
from rest_framework import viewsets


class TeacherRegisterViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = (IsTeacher,)
    serializer_class = TeacherRegisterSerializers
    http_method_names = ['get','post','patch','delete']

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherRegisterSerializers
        elif self.action == 'create':
            return TeacherRegisterSerializers
        elif self.action == 'partial_update':
            return TeacherRegisterSerializers
        elif self.action == 'Destory':
            return TeacherRegisterSerializers
        return TeacherRegisterSerializers
    
    def filter_queryset(self, queryset):
        user = self.request.user 
        return Teacher.objects.filter(user= user)
   




