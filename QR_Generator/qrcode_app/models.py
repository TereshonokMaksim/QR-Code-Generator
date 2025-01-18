from datetime import datetime
from django.db import models

# Create your models here.

class QRCode(models.Model):
    name = models.CharField(max_length = 128)
    size = models.IntegerField()
    color = models.CharField(max_length = 8)
    form = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255)
    path_qrcode = models.ImageField(upload_to = "media/", default = "1")
    when_created = models.DateTimeField(default = datetime.now())
    