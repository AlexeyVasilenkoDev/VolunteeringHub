from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from volunteering.models import Need, Opportunity, Accounting, Category


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('type', 'username', 'email', 'phone', 'is_staff', 'is_active')


class NeedSerializer(ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Need
        fields = '__all__'


class OpportunitySerializer(ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Opportunity
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AccountingSerializer(ModelSerializer):
    class Meta:
        model = Accounting
        fields = '__all__'
