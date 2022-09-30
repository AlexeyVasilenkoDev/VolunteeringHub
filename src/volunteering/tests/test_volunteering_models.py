import time

from django.core.exceptions import ValidationError
from django.test import TestCase

from volunteering.models import Need, Opportunity, Category, Accounting


def sample_category(**params):
    return Category.objects.create(**params)


def sample_opportunity(**params):
    defaults = {
        "description": "Description"
    }
    defaults.update(params)
    return Opportunity.objects.create(**defaults)


def sample_need(**params):
    defaults = {
        "description": "Description"
    }
    defaults.update(params)
    return Need.objects.create(**defaults)


def sample_accounting(**params):
    return Accounting.objects.create(**params)


class TestVolunteeringModels(TestCase):
    def setUp(self) -> None:
        self.test_need = sample_need(title="Need")
        self.test_opportunity = sample_opportunity(title="Opportunity")
        self.test_category = sample_category(name="Category")
        self.test_accounting = sample_accounting(description="Description")
        self.test_need.category.add(self.test_category)
        self.test_need.accounting = self.test_accounting
        self.test_opportunity.category.add(self.test_category)

    def tearDown(self) -> None:
        self.test_need.delete()
        self.test_opportunity.delete()

    def test_fields_validation(self):
        with self.assertRaises(ValidationError):
            sample_category(name="a" * 257)
            sample_need(title="a" * 101)
            sample_opportunity(title="a" * 101)
            sample_need(title=["a"])
            sample_need(title=1)

    def test_relations(self):
        self.assertIsInstance(self.test_need.category.first(), type(self.test_category))
        self.assertIsInstance(self.test_opportunity.category.first(), type(self.test_category))
        self.assertIsInstance(self.test_need.accounting, type(self.test_accounting))

    def test_update(self):
        self.test_need.title = "Test_Update Title"
        self.test_need.save()
        self.assertEqual(self.test_need.title, "Test_Update Title")

    def test_waiting_time(self):
        self.test_need.title = "Test_Update Title"
        self.test_need.save()
        time.sleep(1)
        self.assertEqual(self.test_need.time_waiting().seconds, 1)
