# Generated by Django 4.1.2 on 2022-11-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banking", "0007_bankingmethod_types_alter_bankingmethod_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankingmethod",
            name="logo",
            field=models.ImageField(upload_to="logo"),
        ),
    ]
