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

class News(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name')
    description = models.CharField(max_length=2000, name='description')
    # date = models.DateField(name="date")