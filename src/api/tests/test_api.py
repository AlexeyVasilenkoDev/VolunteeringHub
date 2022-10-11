from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient

from core.utils.test_samples import sample_user, sample_category, sample_accounting, sample_need, sample_opportunity


class Test_API(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.user = sample_user()
        self.user.set_password("password")
        self.user.save()

        self.test_author = sample_user()

        self.test_category = sample_category(name="Category")
        self.test_accounting = sample_accounting(description="Description")

        self.test_need = sample_need(title="Need")
        self.test_need.category.add(self.test_category)
        self.test_need.author.add(self.test_author)
        self.test_need.accounting = self.test_accounting

        self.test_opportunity = sample_opportunity(title="Opportunity", author=self.test_author)
        self.test_opportunity.category.add(self.test_category)

    def test_authorized_user(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:all_opportunities"))
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_unauthorized_user(self):
        result = self.client.get(reverse("api:all_opportunities"))
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def tearDown(self) -> None:
        pass
