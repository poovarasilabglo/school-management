from django.urls import path,include
#from apps.user.views import LoginView
from rest_framework_simplejwt.views import TokenBlacklistView
from apps.user.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshSlidingView
from apps.user.views import ChangePasswordView


urlpatterns = [
    #path('login/', LoginView.as_view()),
    path('token/',MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
]