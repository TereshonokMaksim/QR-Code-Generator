from datetime import datetime
from django.db import models
from django.apps import apps
from user_app.models import Account


class QRCode(models.Model):
    name = models.CharField(max_length = 128)
    size = models.IntegerField()
    color_front = models.CharField(max_length = 8, default = "00000000")
    color_back = models.CharField(max_length = 8, default = "ffffffff")
    form = models.CharField(max_length = 255)
    link = models.TextField()
    path_qrcode = models.ImageField(upload_to = "images/qrcodes/", default = "1")
    when_created = models.DateTimeField(default = datetime.now())
    acc_id = models.ForeignKey(Account, on_delete = models.CASCADE, default = 0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    