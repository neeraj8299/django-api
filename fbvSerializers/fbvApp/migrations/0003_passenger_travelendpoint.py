# Generated by Django 3.2.2 on 2021-05-09 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0002_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='travelEndPoint',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
