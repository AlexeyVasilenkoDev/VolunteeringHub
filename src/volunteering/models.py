from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.db.models import ImageField


class Category(models.Model):
    class CategoryChoices(models.TextChoices):
        MILITARY = 'MIL', _('Military')
        CIVIL = 'CIV', _('Civil')

    name = models.CharField(
        max_length=3,
        choices=CategoryChoices.choices,
    )
    pass


class Opportunity(models.Model):
    category = models.ForeignKey(to="volunteering.Category", related_name="opportunities", on_delete=models.CASCADE)
    description = models.TextField()
    photo = ImageField(upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)


class Need(models.Model):
    category = models.ForeignKey(to="volunteering.Category", related_name="needs", on_delete=models.CASCADE)
    description = models.TextField()
    donation = models.ForeignKey(to="volunteering.Donation", related_name="needs", on_delete=models.CASCADE)
    accounting = models.ForeignKey(to="volunteering.Accounting", related_name="needs", on_delete=models.CASCADE)
    photo = ImageField(upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)


class Donation(models.Model):
    link = models.URLField()


class Accounting(models.Model):
    photo = ImageField(upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    description = models.TextField()
