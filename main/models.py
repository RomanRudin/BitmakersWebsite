from django.db import models

# Create your models here.
class Music(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name')
    description = models.CharField(max_length=2000, name='description')
    # date = models.DateField(name="date")
    # link = models.CharField(max_length=100, name='link')
    # image = models.ImageField(name='image')
    # bit = models.FileField(name='bit')