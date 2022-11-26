from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from core.views import (
    IndexView,
    Login,
    Logout,
    Registration,
    ProfileView,
    NeededView,
    VolunteersView,
    ChangePassword,
    UpdateProfile,
)

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="core"),
    path("registration/", Registration.as_view(), name="registration"),
    path("change_password/", ChangePassword.as_view(), name="change_password"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/<uuid:pk>", ProfileView.as_view(), name="profile"),
    path("profile/update/<uuid:pk>", UpdateProfile.as_view(), name="update_profile"),
    # path("profile/update/<uuid:pk>", UpdateProfile.as_view(), name="update_profile"),
    # path("update_photo/<uuid:pk>", UpdateProfilePhoto, name="UpdateProfilePhoto"),
    path("needed/", NeededView.as_view(), name="NeededView"),
    path("volunteers/", VolunteersView.as_view(), name="VolunteersView"),
]

urlpatterns += staticfiles_urlpatterns()
