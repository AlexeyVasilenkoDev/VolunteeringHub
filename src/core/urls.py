from django.contrib import admin
from django.urls import path

from accounts.views import Registration, IndexView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="core"),
]