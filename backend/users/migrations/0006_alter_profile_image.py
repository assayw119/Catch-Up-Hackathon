# Generated by Django 4.1 on 2022-08-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_profile_star"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.TextField(null=True),
        ),
    ]