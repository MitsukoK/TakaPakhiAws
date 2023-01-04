# Generated by Django 4.1.2 on 2023-01-04 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestMobileRechargeModel",
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
                ("bank_name", models.CharField(max_length=100, null=True)),
                ("amount", models.IntegerField()),
                ("add_logo", models.CharField(max_length=100, null=True)),
                ("ip_address", models.GenericIPAddressField(null=True)),
                ("phone_number", models.CharField(max_length=100)),
                (
                    "choice",
                    models.CharField(
                        choices=[("Prepaid", "Prepaid"), ("Postpaid", "Postpaid")],
                        max_length=10,
                    ),
                ),
                ("is_term", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Declined", "Declined"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Mobile Recharge",
            },
        ),
        migrations.CreateModel(
            name="RequestMobileBankModel",
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
                ("amount", models.IntegerField()),
                ("phone_number", models.CharField(max_length=100)),
                ("bank_name", models.CharField(max_length=100)),
                ("add_logo", models.CharField(max_length=100, null=True)),
                ("ip_address", models.GenericIPAddressField(null=True)),
                (
                    "choice",
                    models.CharField(
                        choices=[("Personal", "Personal"), ("Agent", "Agent")],
                        max_length=10,
                    ),
                ),
                ("is_term", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Declined", "Declined"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Mobile Banking",
                "verbose_name_plural": "Mobile Banking",
            },
        ),
        migrations.CreateModel(
            name="BankingModel",
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
                ("amount", models.IntegerField()),
                ("add_logo", models.CharField(max_length=100, null=True)),
                ("bank_name", models.CharField(max_length=100)),
                ("bank_account_number", models.CharField(max_length=100)),
                ("ip_address", models.GenericIPAddressField(null=True)),
                ("bank_account_name", models.CharField(max_length=100)),
                ("branch_name", models.CharField(max_length=100)),
                ("is_term", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Declined", "Declined"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Banking",
            },
        ),
    ]
