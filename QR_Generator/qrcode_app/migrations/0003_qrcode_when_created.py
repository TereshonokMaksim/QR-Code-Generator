# Generated by Django 5.1.2 on 2025-01-18 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_app', '0002_qrcode_path_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='when_created',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 18, 19, 14, 50, 648975)),
        ),
    ]
