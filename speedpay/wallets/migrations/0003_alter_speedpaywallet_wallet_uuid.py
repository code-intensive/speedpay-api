# Generated by Django 4.1.4 on 2022-12-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wallets", "0002_alter_speedpaywallet_wallet_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="speedpaywallet",
            name="wallet_uuid",
            field=models.CharField(
                db_index=True,
                default="wallet_ad058d58a04842c3851719012793e50a",
                max_length=80,
                verbose_name="user uuid",
            ),
        ),
    ]
