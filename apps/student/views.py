from rest_framework import viewsets
from apps.student.models import(
    Student,
    Subject)
from apps.teacher.models import Teacher
from apps.student.serializers import(
    StudentRegisterSerializers,
    SubjectSerializer)
from apps.user.permissions import(
    IsTeacherOrIsStudent,
    IsTeacher,
)


class StudentRegisterViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = (IsTeacherOrIsStudent,)
    serializer_class = StudentRegisterSerializers
    http_method_names = ['get','post','patch']
    
   
    def get_serializer_class(self):
        if self.action == 'list':
            return StudentRegisterSerializers
        elif self.action == 'create':
            return StudentRegisterSerializers
        elif self.action == 'partial_update':
            return StudentRegisterSerializers
        return StudentRegisterSerializers

    
    def filter_queryset(self, queryset):
        user = self.request.user 
        return Student.objects.filter(user= user)


class StudentListView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = (IsTeacher,)
    serializer_class = StudentRegisterSerializers

    
    def filter_queryset(self, queryset):
        user = self.request.user 
        print(user)
        return Student.objects.filter(teacher= Teacher.objects.get(user = self.request.user))


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = (IsTeacherOrIsStudent,)
    serializer_class = SubjectSerializer

    
    def perform_create(self, serializer):
        serializer.save(teacher= Teacher.objects.get(user = self.request.user))

    
    def filter_queryset(self, queryset):
        if self.request.user.is_teacher == True:
            return Subject.objects.filter(teacher = Teacher.objects.get(user = self.request.user ))
        elif self.request.user.is_student == True:
            return Subject.objects.filter(student__user = self.request.user)
        # elif self.request.user.is_parent == True:
        #     return Subject.objects.filter(student= Student.objects.get(user = self.request.user))
        return super().filter_queryset(queryset)

    


