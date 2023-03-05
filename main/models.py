from django.db import models
import datetime

'''
After test, please, DELETE ALL THE DEFAULT VALUES ON THIS LEVEL             I
'''
class Beats(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name',  default="Жаль")
    description = models.CharField(max_length=2000, name='description',     default="The best song in history of humanity")
    date = models.DateField(name="date", default=datetime.date.today)
    # link = models.CharField(max_length=100, name='link')
    # image = models.ImageField(name='image')
    # beat = models.FileField(name='beat')
    # beatogg = models.FileField(name='beatogg')
    license_mp3 = models.BooleanField(name="license_mp3", default=False)
    license_wav = models.BooleanField(name="license_wav", default=False)
    license_trackout = models.BooleanField(name="license_trackout", default=False)
    license_unlimited = models.BooleanField(name="license_unlimited", default=False)
    license_exclisive = models.BooleanField(name="license_exclisive", default=False)


'''
After test, please, DELETE ALL THE DEFAULT VALUES ON THIS LEVEL
'''
class Tracks(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name',  default="Жаль")
    description = models.CharField(max_length=2000, name='description',     default="The best song in history of humanity")
    date = models.DateField(name="date", default=datetime.date.today)
    # link = models.CharField(max_length=100, name='link')
    # image = models.ImageField(name='image')
    # track = models.FileField(name='track')
    # trackogg = models.FileField(name='trackogg')


'''
After test, please, DELETE ALL THE DEFAULT VALUES ON THIS LEVEL             I
'''
class News(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name='name',  default="NEW RELEASE! TODAY!")
    description = models.CharField(max_length=2000, name='description',     default="Ты думал здесь что-то будет?")
    date = models.DateField(name="date", default=datetime.date.today)


'''
After test, please, DELETE ALL THE DEFAULT VALUES ON THIS LEVEL             I
'''
class Links(models.Model):
    name = models.CharField(primary_key=True, max_length=100, name="name",  default="VK")
    link = models.CharField(max_length=2000, name='link',                   default="https://vk.com/")
    #icon = models.ImageField(name="icon")