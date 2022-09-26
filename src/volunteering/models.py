from django.db import models
# Create your models here.
from django.db.models import ImageField


class Category(models.Model):
    name = models.CharField(
        max_length=256,
    )


class Opportunity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = ImageField(upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    category = models.ForeignKey(to="volunteering.Category", related_name="opportunities", on_delete=models.CASCADE)


class Need(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField()
    donation = models.URLField()
    accounting = models.ForeignKey(to="volunteering.Accounting", related_name="needs", on_delete=models.CASCADE)
    photo = ImageField(upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    category = models.ManyToManyField(to="volunteering.Category", related_name="needs", )


class Accounting(models.Model):
    photo = ImageField(upload_to="",  # TODO upload_to related to needs
                       blank=True,
                       null=True)
    description = models.TextField()
