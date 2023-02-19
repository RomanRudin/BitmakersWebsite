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
    license_mp3 = models.BooleanField(name="license_mp3", default=False)
    license_wav = models.BooleanField(name="license_wav", default=False)
    license_trackout = models.BooleanField(name="license_trackout", default=False)
    license_unlimited = models.BooleanField(name="license_unlimited", default=False)
    license_exclisive = models.BooleanField(name="license_exclisive", default=False)

class News(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name')
    description = models.CharField(max_length=2000, name='description')
    # date = models.DateField(name="date")