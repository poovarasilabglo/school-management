from rest_framework import serializers
from apps.teacher.models import Teacher
from apps.user.serializers import TeacherSerializer


class TeacherRegisterSerializers(serializers.ModelSerializer):
    user = TeacherSerializer(required = True)
    class Meta:
        model = Teacher
        fields = ('user',
                  'teacher_id',
                  'name',
                  'image',
                  'dob',
                  'gender',
                  'phone',
                  'address',
                  'join_year')

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = TeacherSerializer.create(TeacherSerializer(),validated_data= user_data)
        return Teacher.objects.create(**validated_data, user= user)