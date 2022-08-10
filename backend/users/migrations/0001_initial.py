# Generated by Django 4.1 on 2022-08-10 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=10)),
                ("nickname", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("introduction", models.TextField(default="", null=True)),
                ("image", models.ImageField(null=True, upload_to="")),
                ("coin", models.IntegerField()),
                ("star", models.FloatField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]