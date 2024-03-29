from django.urls import path
from .views import (
    user_login,
    user_logout,
    user_register,
    user_profile,
    verify_email,
    resend_otp,
)

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
    path("profile/", user_profile, name="profile"),
    path("verify-email/", verify_email, name="verify-email"),
    path("resend-otp/", resend_otp, name="resend-otp"),
]
