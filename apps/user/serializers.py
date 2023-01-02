from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from apps.user.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['role'] = cls.get_role(user)
        return token
    
    @classmethod
    def get_role(cls,user):
        if user.is_staff:
            return "admin"
        elif user.is_student:
            return "student"
        elif user.is_teacher:
            return "teacher"
        elif user.is_accountant:
            return "accountant"
        elif user.is_parent:
            return "parent"


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required = True,
                                     validators = [validate_password])
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_student',
                 )

    def create(self,validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class TeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required = True,
                                     validators = [validate_password])
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_teacher',
                 )

    def create(self,validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


# __change_password__
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = '__all__' 
