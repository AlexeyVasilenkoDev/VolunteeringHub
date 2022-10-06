from django.urls import path

from accounts.views import IndexView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="core"),
]
