from unicodedata import name
from django.db import models
from numpy import true_divide

# Create your models here.
class Music(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name')
    description = models.CharField(max_length=2000, name='description')
    # date = models.DateField(name="date")
    # link = models.CharField(max_length=100, name='link')
    # image = models.ImageField(name='image')
    # bit = models.FileField(name='bit')
    # bitogg = models.FileField(name='bitogg')
    license_mo3 = models.BooleanField(name="license_mo3")
    license_wav = models.BooleanField(name="license_wav")
    license_trackout = models.BooleanField(name="license_trackout")
    license_unlimited = models.BooleanField(name="license_unlimited")
    license_exclisive = models.BooleanField(name="license_exclisive")

class News(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name')
    description = models.CharField(max_length=2000, name='description')
    # date = models.DateField(name="date")