# Generated by Django 3.1 on 2020-08-19 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_eventcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='premium_applied',
            field=models.BooleanField(default=False),
        ),
    ]
