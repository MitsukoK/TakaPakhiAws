# Generated by Django 4.1.2 on 2022-11-29 06:01

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0005_remove_newuser_bank_remove_newuser_mobile_banking_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="newuser",
            name="bank",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Asia Bank", "Asia Bank"),
                    ("Brack Bank", "Brack Bank"),
                    ("City Bank", "City Bank"),
                    ("DBBL", "DBBL"),
                    ("EBL", "EBL"),
                    ("Exim Bank", "Exim Bank"),
                    ("Islami Bank", "Islami Bank"),
                    ("Mutual Trust Bank", "Mutual Trust Bank"),
                    ("One Bank", "One Bank"),
                    ("Prime Bank", "Prime Bank"),
                    ("UCB Bank", "UCB Bank"),
                ],
                default="Asia Bank",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="newuser",
            name="mobile_banking",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Mkash", "Mkash"),
                    ("Bkash", "Bkash"),
                    ("Roket", "Roket"),
                    ("Upay", "Upay"),
                    ("Surecash", "Surecash"),
                    ("Nagad", "Nagad"),
                ],
                default="Mkash",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="newuser",
            name="mobile_recharge",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Banglalink", "Banglalink"),
                    ("Airtel", "Airtel"),
                    ("Grameenphone", "Grameenphone"),
                    ("Teletalk", "Teletalk"),
                    ("Robi", "Robi"),
                ],
                default="Banglalink",
                max_length=100,
            ),
        ),
    ]
