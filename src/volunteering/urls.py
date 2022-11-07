from django.urls import path

from volunteering.views import CreateNeed, AllNeeds, user_generator, category_generator, accounting_generator, \
    need_generator, opportunity_generator

app_name = "volunteering"

urlpatterns = [
    path("", AllNeeds.as_view(), name="needs"),
    path("create/", CreateNeed.as_view(), name="create_need"),

    path("generate/user", user_generator, name="user_generator"),
    path("generate/category", category_generator, name="category_generator"),
    path("generate/accounting", accounting_generator, name="accounting_generator"),
    path("generate/need", need_generator, name="need_generator"),
    path("generate/opportunity", opportunity_generator, name="opportunity_generator"),
]
