from rest_framework import serializers
from apps.user.serializers import StudentSerializer
from apps.student.models import Student,Subject


class StudentRegisterSerializers(serializers.ModelSerializer):
    user = StudentSerializer(required = True)
    class Meta:
        model = Student
        fields = ('user',
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
                  'roll_number')

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = StudentSerializer.create(StudentSerializer(), validated_data= user_data)
        return Student.objects.create(**validated_data, user= user)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
