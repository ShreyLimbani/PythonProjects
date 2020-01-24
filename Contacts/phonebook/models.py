from django.db import models


# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    countryCode1 = models.CharField(max_length=4)
    mobileNumber1 = models.IntegerField()
    #countryCode2 = models.CharField(max_length=4)
    #mobileNumber2 = models.IntegerField()
    email = models.EmailField()
    dateOfBirth = models.DateField()
    #website = models.URLField()