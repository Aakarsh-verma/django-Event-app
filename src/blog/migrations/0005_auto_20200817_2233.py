# Generated by Django 3.1 on 2020-08-17 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_eventcategory'),
        ('blog', '0004_auto_20200817_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='related_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.eventpost'),
        ),
    ]
