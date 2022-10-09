"""config URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers

from api.views import UserViewSet, CreateNeedView, CreateOpportunityView, CreateCategoryView, CreateAccountingView, \
    RetrieveNeedView, UpdateNeedView, DeleteNeedView, RetrieveOpportunityView, UpdateOpportunityView, \
    DeleteOpportunityView, RetrieveCategoryView, UpdateCategoryView, DeleteCategoryView, UpdateAccountingView, \
    RetrieveAccountingView, DeleteAccountingView, AllNeedsView, AllOpportunitiesView, AllCategoriesView, \
    AllAccountingView

app_name = "api"
routes = routers.DefaultRouter()
routes.register("users", UserViewSet)

urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),

    path("needs/", AllNeedsView.as_view(), name="all_needs"),
    path("needs/<int:pk>/", RetrieveNeedView.as_view(), name="need"),
    path("needs/create/", CreateNeedView.as_view(), name="create_need"),
    path("needs/update/<int:pk>/", UpdateNeedView.as_view(), name="update_need"),
    path("needs/delete/<int:pk>/", DeleteNeedView.as_view(), name="delete_need"),

    path("opportunities/", AllOpportunitiesView.as_view(), name="all_opportunities"),
    path("opportunities/<int:pk>/", RetrieveOpportunityView.as_view(), name="all_opportunities"),
    path("opportunities/create/", CreateOpportunityView.as_view(), name="create_opportunity"),
    path("opportunities/update/<int:pk>/", UpdateOpportunityView.as_view(), name="update_opportunity"),
    path("opportunities/delete/<int:pk>/", DeleteOpportunityView.as_view(), name="delete_opportunity"),

    path("categories/", AllCategoriesView.as_view(), name="all_categories"),
    path("categories/<int:pk>/", RetrieveCategoryView.as_view(), name="category"),
    path("categories/create/", CreateCategoryView.as_view(), name="create_category"),
    path("categories/update/<int:pk>/", UpdateCategoryView.as_view(), name="update_category"),
    path("categories/delete/<int:pk>/", DeleteCategoryView.as_view(), name="delete_category"),

    path("accounting/", AllAccountingView.as_view(), name="all_accounting"),
    path("accounting/<int:pk>/", RetrieveAccountingView.as_view(), name="accounting"),
    path("accounting/create/", CreateAccountingView.as_view(), name="create_accounting"),
    path("accounting/update/<int:pk>/", UpdateAccountingView.as_view(), name="update_accounting"),
    path("accounting/delete/<int:pk>/", DeleteAccountingView.as_view(), name="delete_accounting"),
]
