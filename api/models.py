from django.db import models

# Create your models here.


class Timer(models.Model):
    json = models.JSONField()
