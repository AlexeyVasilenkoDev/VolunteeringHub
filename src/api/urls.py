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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (AllAccountingView, AllCategoriesView, AllNeedsView,
                       AllOpportunitiesView, CreateAccountingView,
                       CreateCategoryView, CreateNeedView,
                       CreateOpportunityView, DeleteAccountingView,
                       DeleteCategoryView, DeleteNeedView,
                       DeleteOpportunityView, RetrieveAccountingView,
                       RetrieveCategoryView, RetrieveNeedView,
                       RetrieveOpportunityView, UpdateAccountingView,
                       UpdateCategoryView, UpdateNeedView,
                       UpdateOpportunityView, UserViewSet)

app_name = "api"
routes = routers.DefaultRouter()
routes.register("users", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="VolunteeringHub API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("", include(routes.urls)),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls.jwt")),

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
