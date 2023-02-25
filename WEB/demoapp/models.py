from django.db import models

# Create your models here.


class patient(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=1, null=False)
    doctor = models.CharField(max_length=50, null=False)
    date = models.IntegerField(null=False)



class bed(models.Model):
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    city = models.CharField(max_length=50, null=False)
    country =  models.CharField(max_length=50, null=False)

class patient_data(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=1, null=False)
    doctor = models.CharField(max_length=50, null=False)
    date = models.CharField(max_length=10, null=False)