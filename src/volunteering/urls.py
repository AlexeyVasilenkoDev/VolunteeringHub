from django.urls import path

from volunteering.views import CreateNeed, AllNeeds

app_name = "volunteering"

urlpatterns = [
    path("", AllNeeds.as_view(), name="needs"),
    path("create/", CreateNeed.as_view(), name="create_need"),
]