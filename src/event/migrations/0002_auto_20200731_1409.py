# Generated by Django 3.0.8 on 2020-07-31 08:39

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='image',
            field=models.ImageField(default='pce_logo.png', upload_to=event.models.upload_location),
        ),
    ]
