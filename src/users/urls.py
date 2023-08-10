from django.urls import path

from users.views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path("registration", UserRegistrationAPIView.as_view(), name="user-registration"),
    path("login", UserLoginAPIView.as_view(), name="user-login")
]
