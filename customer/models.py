from django.db import models

# Create your models here.

GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


class Customer(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='name', blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, verbose_name='address', blank=True)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True)
    status = models.CharField(max_length=30, verbose_name='marital status', blank=True)

    def __str__(self):
        return str(self.name)+" : "+str(self.email)+" : "+str(self.phone)+" : "+str(self.address)+" : "+str(self.gender)+" : "+str(self.status)

