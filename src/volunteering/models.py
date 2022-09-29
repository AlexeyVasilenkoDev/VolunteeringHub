from django.db import models
# Create your models here.

from django.db.models import ImageField
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("name"), max_length=256, )


class Opportunity(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"), )
    photo = ImageField(_("photo"),
                       upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    category = models.ManyToManyField(to="volunteering.Category", related_name="opportunities", )
    city = models.CharField(_("city"), max_length=150, blank=True, null=True, default=None)


class Need(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"), )
    price = models.DecimalField(_("price"), decimal_places=2, max_digits=20, null=True, blank=True)
    donation = models.URLField(_("donation"), null=True, blank=True)
    accounting = models.ForeignKey(to="volunteering.Accounting", related_name="needs",
                                   on_delete=models.CASCADE)
    photo = ImageField(_("photo"), upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    category = models.ManyToManyField(to="volunteering.Category", related_name="needs", )
    city = models.CharField(_("city"), max_length=150, blank=True, null=True, default=None)


class Accounting(models.Model):
    photo = ImageField(_("photo"), upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    description = models.TextField(_("description"), )
