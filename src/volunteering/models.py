from django.db import models
# Create your models here.

from django.db.models import ImageField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Saver(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Category(Saver):
    name = models.CharField(_("name"), max_length=256, )


class Opportunity(Saver):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"), )
    photo = ImageField(_("photo"),
                       upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    category = models.ManyToManyField(to="volunteering.Category", related_name="category", )
    city = models.CharField(_("city"), max_length=150, blank=True, null=True, default=None)
    author = models.ForeignKey(to="accounts.CustomUser", related_name="opportunity_author", on_delete=models.CASCADE,
                               null=False, blank=False)


class Need(Saver):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"), )
    price = models.DecimalField(_("price"), decimal_places=2, max_digits=20, null=True, blank=True)
    donation = models.URLField(_("donation"), null=True, blank=True)
    accounting = models.ForeignKey(to="volunteering.Accounting", related_name="needs",
                                   on_delete=models.CASCADE, null=True, blank=True)
    photo = ImageField(_("photo"), upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    category = models.ManyToManyField(to="volunteering.Category", related_name="needs", blank=True, null=True, )
    city = models.CharField(_("city"), max_length=150, blank=True, null=True, default=None)
    author = models.ManyToManyField(to="accounts.CustomUser", related_name="need_author", null=False, blank=False)

    def save(self, *args, **kwargs):
        self.full_clean()
        self.time_created = timezone.now()
        return super().save(*args, **kwargs)

    def time_waiting(self):
        return timezone.now() - self.time_created


class Accounting(Saver):
    photo = ImageField(_("photo"), upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    description = models.TextField(_("description"), max_length=256, )
