# Generated by Django 5.1.2 on 2025-03-02 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_app', '0012_qrcode_active_alter_qrcode_when_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='when_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
