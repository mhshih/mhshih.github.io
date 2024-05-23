from django.db import models

class User(models.Model):
    username = models.CharField(max_length=333)
    email = models.CharField(max_length=333)