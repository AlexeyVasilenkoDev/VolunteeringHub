from django.urls import path

from volunteering.views import CreateNeed, AllNeeds, AllOpportunities, CreateOpportunity, AllAccounting, \
    CreateAccounting, user_generator, category_generator, accounting_generator, \
    need_generator, opportunity_generator

app_name = "volunteering"

urlpatterns = [

    path("", AllNeeds.as_view(), name="needs"),
    path("create/", CreateNeed.as_view(), name="create_need"),

    path("needs/", AllNeeds.as_view(), name="needs"),
    path("needs/create/", CreateNeed.as_view(), name="create_need"),
    # path("needs/update/", UpdateNeed.as_view(), name="update_need"),

    path("opportunities/", AllOpportunities.as_view(), name="opportunities"),
    path("opportunities/create", CreateOpportunity.as_view(), name="create_opportunity"),
    # path("opportunities/update", UpdateNeed.as_view(), name="update_need"),

    path("accounting/", AllAccounting.as_view(), name="accounting"),
    path("accounting/create", CreateAccounting.as_view(), name="create_accounting"),
    # path("opportunities/update", UpdateNeed.as_view(), name="update_need"),

    path("generate/user", user_generator, name="user_generator"),
    path("generate/category", category_generator, name="category_generator"),
    path("generate/accounting", accounting_generator, name="accounting_generator"),
    path("generate/need", need_generator, name="need_generator"),
    path("generate/opportunity", opportunity_generator, name="opportunity_generator"),
]
