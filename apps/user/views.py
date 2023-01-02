# from django.shortcuts import render
# from rest_framework import views
#from django.contrib.auth import authenticate
# from django.contrib.auth import login
# from apps.user.utils import get_tokens_for_user
# from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.user.serializers import MyTokenObtainPairSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
''' change_password '''
from rest_framework import generics
from apps.user.models import User
from apps.user.serializers import ChangePasswordSerializer
#from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response


'''class LoginView(views.APIView):
    def post(self, request):
        data = request.data
        if 'username' not in data or 'password' not in data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(user)
            return Response({**auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)'''


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    @swagger_auto_schema(
    response_token = {
    "200": openapi.Response(
        description="Response for successful token creation",
        examples={
            "application/json": {
                "refresh": "<refresh_token>",
                "access": "<access_token>",
            }
        },
    ),
    "401": openapi.Response(
        description="Response for successful invalid credentials",
        examples={
            "application/json": {
                "detail": "No active account found with the given credentials"
            }
        },
    ),
}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    #permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




