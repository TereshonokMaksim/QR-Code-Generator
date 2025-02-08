from datetime import datetime
from django.db import models
from django.apps import apps
from user_app.models import Account


class QRCode(models.Model):
    name = models.CharField(max_length = 128)
    size = models.IntegerField()
    color = models.CharField(max_length = 8)
    form = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255)
    path_qrcode = models.ImageField(upload_to = "images/qrcodes/", default = "1")
    when_created = models.DateTimeField(default = datetime.now())
    acc_id = models.ForeignKey(Account, on_delete = models.CASCADE, default = 0)

    def __str__(self):
        return self.name
    