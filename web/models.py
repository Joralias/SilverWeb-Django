from django.db import models
from django.utils import timezone


class Fan(models.Model):
    mail = models.EmailField(max_length=254)

    def __str__(self):
        return self.mail


class Message(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    mail = models.EmailField(max_length=254)
    created_date = models.DateTimeField(
            default=timezone.now)
