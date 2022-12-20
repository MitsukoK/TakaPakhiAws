# Generated by Django 4.1.2 on 2022-12-20 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_request", "0005_requestmobilebankmodel_bank_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="bankingmodel",
            name="add_logo",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="requestmobilebankmodel",
            name="add_logo",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="requestmobilerechargemodel",
            name="add_logo",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="NotificationModel",
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
                (
                    "status",
                    models.CharField(
                        choices=[("read", "Read"), ("unread", "Unread")], max_length=20
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bank",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_request.bankingmodel",
                    ),
                ),
                (
                    "mobile_bank",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_request.requestmobilebankmodel",
                    ),
                ),
                (
                    "recharge",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_request.requestmobilerechargemodel",
                    ),
                ),
            ],
        ),
    ]