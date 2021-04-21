from django.db import models

# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=15)
    birthday = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)

