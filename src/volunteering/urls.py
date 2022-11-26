from django.urls import path

from volunteering.views import (
    CreateNeed,
    AllNeeds,
    AllOpportunities,
    CreateOpportunity,
    AllAccounting,
    CreateAccounting,
    user_generator,
    category_generator,
    accounting_generator,
    need_generator,
    opportunity_generator,
    NeedView,
    OpportunityView,
    AccountingView,
    UpdateNeed,
    UpdateAccounting,
    UpdateOpportunity,
    DeleteAccounting,
    DeleteNeed,
    DeleteOpportunity,
    CategoryView,
    AllCategories, HintNeed, CategoryNeeds, CategoryOpportunities,
)

app_name = "volunteering"

urlpatterns = [
    path("needs/", AllNeeds.as_view(), name="needs"),
    path("needs/<int:pk>", NeedView.as_view(), name="need"),
    path("needs/create/", CreateNeed.as_view(), name="create_need"),
    path("needs/update/<int:pk>", UpdateNeed.as_view(), name="update_need"),
    path("needs/delete/<int:pk>", DeleteNeed.as_view(), name="delete_need"),

    path("opportunities/", AllOpportunities.as_view(), name="opportunities"),
    path("opportunities/<int:pk>", OpportunityView.as_view(), name="opportunity"),
    path("opportunities/create", CreateOpportunity.as_view(), name="create_opportunity"),
    path("opportunities/update/<int:pk>", UpdateOpportunity.as_view(), name="update_opportunity"),
    path("opportunities/delete/<int:pk>", DeleteOpportunity.as_view(), name="delete_opportunity"),

    path("accounting/", AllAccounting.as_view(), name="accounting"),
    path("accounting/<int:pk>", AccountingView.as_view(), name="account"),
    path("accounting/create", CreateAccounting.as_view(), name="create_accounting"),
    path("accounting/update/<int:pk>", UpdateAccounting.as_view(), name="update_accounting"),
    path("accounting/delete/<int:pk>", DeleteAccounting.as_view(), name="delete_accounting"),

    path("categories/", AllCategories.as_view(), name="categories"),
    path("category/<str:name>", CategoryView.as_view(), name="category"),
    path("category/needs/<str:name>", CategoryNeeds.as_view(), name="category_needs"),
    path("category/opportunities/<str:name>", CategoryOpportunities.as_view(), name="category_opportunities"),

    path("needs/hint/<int:pk>", HintNeed.as_view(), name="hint_need"),

    path("generate/user", user_generator, name="user_generator"),
    path("generate/category", category_generator, name="category_generator"),
    path("generate/accounting", accounting_generator, name="accounting_generator"),
    path("generate/need", need_generator, name="need_generator"),
    path("generate/opportunity", opportunity_generator, name="opportunity_generator"),
]
