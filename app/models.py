from django.db import models


# Create your models here.
class RegistrationData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobile = models.BigIntegerField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=100)
