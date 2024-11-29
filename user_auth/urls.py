from django.urls import path
from .views import signup, login, logout_user, user_profile, edit_user_profile

urlpatterns = [
    path("signup/", signup, name="signup" ),
    path("login/", login, name="login"),
    path("logout/", logout_user, name="logout"),
    path("user_profile", user_profile, name="user_profile" ),
    path('edit_user_profile/', edit_user_profile, name="edit_user_profile" ),
]


