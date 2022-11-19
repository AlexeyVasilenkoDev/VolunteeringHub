from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from core.views import IndexView, Login, Logout, Registration, ProfileView, UpdateProfilePhoto, NeededView, \
    VolunteersView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="core"),
    path("registration/", Registration.as_view(), name="registration"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/<uuid:pk>", ProfileView.as_view(), name="profile"),
    path("update_photo/<uuid:pk>", UpdateProfilePhoto, name="UpdateProfilePhoto"),
    path("needed/", NeededView.as_view(), name="NeededView"),
    path("volunteers/", VolunteersView.as_view(), name="VolunteersView"),
]

urlpatterns += staticfiles_urlpatterns()
