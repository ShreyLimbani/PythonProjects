from django.db import models


# Create your models here.
class ContactManager(models.Manager):
    def create_contact(self, firstName, lastName, mobileNumber1, email, dateOfBirth):
        contact = self.create(firstName=firstName, lastName=lastName, mobileNumber1=mobileNumber1, email=email,
                              dateOfBirth=dateOfBirth)
        return contact

    def getCon(self,mobileNumber1):
        contact = self.get(mobileNumber1=mobileNumber1)
        return contact

class Contact(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    countryCode1 = models.CharField(max_length=4)
    mobileNumber1 = models.IntegerField()
    # countryCode2 = models.CharField(max_length=4)
    # mobileNumber2 = models.IntegerField()
    email = models.EmailField()
    dateOfBirth = models.DateField()
    # website = models.URLField()

    object = ContactManager()
