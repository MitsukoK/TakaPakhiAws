# Generated by Django 4.1.2 on 2022-11-15 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "user_request",
            "0002_bankingmodel_status_requestmobilebankmodel_status_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankingmodel",
            name="is_term",
            field=models.BooleanField(),
        ),
    ]
