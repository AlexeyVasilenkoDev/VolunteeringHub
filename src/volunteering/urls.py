from django.urls import path

from volunteering.views import CreateNeed, AllNeeds, AllOpportunities, CreateOpportunity, AllAccounting, \
    CreateAccounting

app_name = "volunteering"

urlpatterns = [
    path("needs/", AllNeeds.as_view(), name="needs"),
    path("needs/create/", CreateNeed.as_view(), name="create_need"),
    # path("needs/update/", UpdateNeed.as_view(), name="update_need"),

    path("opportunities/", AllOpportunities.as_view(), name="opportunities"),
    path("opportunities/create", CreateOpportunity.as_view(), name="create_opportunity"),
    # path("opportunities/update", UpdateNeed.as_view(), name="update_need"),

    path("accounting/", AllAccounting.as_view(), name="accounting"),
    path("accounting/create", CreateAccounting.as_view(), name="create_accounting"),
    # path("opportunities/update", UpdateNeed.as_view(), name="update_need"),

]
