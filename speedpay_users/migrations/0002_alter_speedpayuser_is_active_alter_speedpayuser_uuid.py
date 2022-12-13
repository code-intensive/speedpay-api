# Generated by Django 4.1.4 on 2022-12-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("speedpay_users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="speedpayuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="speedpayuser",
            name="uuid",
            field=models.CharField(
                db_index=True,
                default="user_bd537126583f4bc085e91a70d7d7645f",
                max_length=80,
            ),
        ),
    ]