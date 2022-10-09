from django.urls import path

from core.views import IndexView, Registration, Login, Logout

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="core"),
    path("registration/", Registration.as_view(), name="registration"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
