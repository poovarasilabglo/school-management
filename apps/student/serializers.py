from rest_framework import serializers
from apps.user.serializers import StudentSerializer
from apps.student.models import Student,Subject


class StudentRegisterSerializers(serializers.ModelSerializer):
    user = StudentSerializer(required = True)
    class Meta:
        model = Student
        fields = ('user',
                  'teacher',
                  'id',
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
                  'roll_number',
                 )


    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = StudentSerializer.create(StudentSerializer(), validated_data= user_data)
        return Student.objects.create(**validated_data, user= user)


class SubjectSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.username', read_only = True)
    class Meta:
        model = Subject
        fields = ('id',
                  #'teacher',
                  'student',
                  'student_name',
                  'subject_code',
                  'subject_name',
                  'subject_mark',
                  )
