from django.urls import path

from core.views import IndexView, Registration

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="core"),
    path("registration/", Registration.as_view(), name="registration"),
]
