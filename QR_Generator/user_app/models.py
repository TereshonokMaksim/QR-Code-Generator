from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Subscription(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    max_qrcodes = models.IntegerField()
    can_customize = models.BooleanField(default = True)

    def __str__(self):
        return self.title

class Account(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    verified = models.IntegerField()
    subscription = models.ForeignKey(Subscription, on_delete = models.SET_NULL, null = True)
    sub_expire = models.DateTimeField(default = datetime.now())

    def get_absolute_url(self):
        return reverse('confirm_email', kwargs = {'verification_code': self.verified})

    def __str__(self):
        return self.user.username