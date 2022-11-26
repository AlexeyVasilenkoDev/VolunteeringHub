# Generated by Django 4.1.1 on 2022-11-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=models.ImageField(
                blank=True,
                default="profile/profile_default.png",
                null=True,
                upload_to="profile/",
            ),
        ),
    ]
