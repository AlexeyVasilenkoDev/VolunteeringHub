from django.db import models
from django.db.models import ImageField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField


# Create your models here.


class Saver(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Category(Saver):
    name = models.CharField(
        _("name"),
        max_length=256,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Opportunity(Saver):
    title = models.CharField(_("title"), max_length=100)
    description = QuillField(_("description"), blank=True, null=True, default=None)
    category = models.ManyToManyField(
        to="volunteering.Category",
        related_name="category",
    )
    city = models.CharField(_("city"), max_length=150, blank=True, null=True, default=None)
    author = models.ForeignKey(
        to="accounts.CustomUser", related_name="opportunity_author", on_delete=models.CASCADE, null=False, blank=False
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Opportunities"


class Need(Saver):
    title = models.CharField(_("title"), max_length=100)
    description = QuillField(_("description"), blank=True, null=True, default=None)
    price = models.DecimalField(_("price"), decimal_places=2, max_digits=20, null=True, blank=True)
    donation = models.URLField(_("donation"), null=True, blank=True)
    accounting = models.ForeignKey(
        to="volunteering.Accounting", related_name="needs", on_delete=models.CASCADE, null=True, blank=True
    )
    category = models.ManyToManyField(
        to="volunteering.Category",
        related_name="needs",
        blank=True,
        null=True,
    )
    city = models.CharField(_("city"), max_length=150, blank=True, null=True, default=None)
    author = models.ForeignKey(to="accounts.CustomUser", related_name="need_author", on_delete=models.CASCADE,
                               null=False, blank=False)
    is_satisfied = models.BooleanField(null=False, blank=False, default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.title) or ""

    def time_waiting(self):
        return timezone.now() - self.date_created


class Accounting(Saver):
    description = QuillField(_("description"), blank=True, null=True, default=None)
    author = models.ForeignKey(
        to="accounts.CustomUser", related_name="accounting_author", on_delete=models.CASCADE, null=False, blank=False
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Accounting"
