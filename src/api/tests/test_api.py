from unittest.mock import ANY

from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient
import testing.postgresql

from core.utils.test_samples import sample_accounting, sample_category, sample_need, sample_opportunity, sample_user


class Test_API(TestCase):
    def setUp(self) -> None:
        self.postgresql = testing.postgresql.Postgresql()

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

    def test_need_retrieve(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:need", kwargs={"pk": self.test_category.pk}))
        self.assertEqual(
            result.data,
            {
                "id": ANY,
                "category": ["Category"],
                "title": "Need",
                "description": "Description",
                "price": None,
                "donation": None,
                "photo": None,
                "accounting": None,
                "city": None,
                "author": [ANY],
            },
        )

    def test_need_create(self):
        self.client.force_authenticate(user=self.user)
        need_created = self.client.post(
            reverse("api:create_need"),
            data={
                "category": ["Category1"],
                "title": "Need2",
                "description": "Description2",
                "price": 100.00,
                "donation": "https://google.com",
                "photo": "",
                "accounting": "",
                "city": "",
                "author": [1],
            },
        )
        self.assertEqual(need_created.status_code, HTTP_201_CREATED)

    def test_product_delete(self):
        self.client.force_authenticate(user=self.user)
        self.need = sample_need(title="Need2", description="Description2")
        self.need.category.add(self.test_category)
        need_deleted = self.client.delete(reverse("api:delete_need", kwargs={"pk": self.need.pk}))
        self.assertEqual(need_deleted.status_code, HTTP_204_NO_CONTENT)

    def tearDown(self) -> None:
        self.postgresql.stop()
        self.test_need.delete()
        self.test_opportunity.delete()
        self.test_category.delete()
        self.test_accounting.delete()
        self.test_author.delete()
