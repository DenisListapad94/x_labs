from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from ..views.auth_views import RegisterUserApiView

urlpatterns = [
    path('register/', RegisterUserApiView.as_view(), name="sign_up"),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
