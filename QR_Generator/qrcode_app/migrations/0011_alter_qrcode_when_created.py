# Generated by Django 5.1.4 on 2025-02-25 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_app', '0010_alter_qrcode_when_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='when_created',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 25, 19, 9, 11, 896218)),
        ),
    ]
