# Generated by Django 3.1 on 2020-09-02 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_account_from_pce'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='post_limit',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
