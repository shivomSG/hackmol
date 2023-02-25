from django.db import models

# Create your models here.


class patient(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=1, null=False)
    doctor = models.CharField(max_length=50, null=False)
    date = models.IntegerField(null=False)


