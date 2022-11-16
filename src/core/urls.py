from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from core.views import IndexView, Login, Logout, Registration, ProfileView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="core"),
    path("registration/", Registration.as_view(), name="registration"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/<uuid:pk>", ProfileView.as_view(), name="profile"),
]

urlpatterns += staticfiles_urlpatterns()
