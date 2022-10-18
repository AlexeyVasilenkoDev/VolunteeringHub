from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.serializers import (
    AccountingSerializer,
    CategorySerializer,
    NeedSerializer,
    OpportunitySerializer,
    UserSerializer,
)
from volunteering.models import Accounting, Category, Need, Opportunity


class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class NeedsView:
    queryset = Need.objects.all()
    serializer_class = NeedSerializer


class OpportunitiesView:
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


class CategoriesView:
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AccountingView:
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer


"""Need"""


class CreateNeedView(NeedsView, CreateAPIView):
    pass


class AllNeedsView(NeedsView, ListAPIView):
    permission_classes = [AllowAny]
    pass


class RetrieveNeedView(NeedsView, RetrieveAPIView):
    pass


class UpdateNeedView(NeedsView, UpdateAPIView):
    pass


class DeleteNeedView(NeedsView, DestroyAPIView):
    pass


"""Opportunity"""


class CreateOpportunityView(OpportunitiesView, CreateAPIView):
    pass


class AllOpportunitiesView(OpportunitiesView, ListAPIView):
    pass


class RetrieveOpportunityView(OpportunitiesView, RetrieveAPIView):
    pass


class UpdateOpportunityView(OpportunitiesView, UpdateAPIView):
    pass


class DeleteOpportunityView(OpportunitiesView, DestroyAPIView):
    pass


"""Category"""


class CreateCategoryView(CategoriesView, CreateAPIView):
    pass


class AllCategoriesView(CategoriesView, ListAPIView):
    pass


class RetrieveCategoryView(CategoriesView, RetrieveAPIView):
    pass


class UpdateCategoryView(CategoriesView, UpdateAPIView):
    pass


class DeleteCategoryView(DestroyAPIView):
    pass


"""Accounting"""


class CreateAccountingView(AccountingView, CreateAPIView):
    pass


class AllAccountingView(AccountingView, ListAPIView):
    pass


class RetrieveAccountingView(AccountingView, RetrieveAPIView):
    pass


class UpdateAccountingView(AccountingView, UpdateAPIView):
    pass


class DeleteAccountingView(AccountingView, DestroyAPIView):
    pass
