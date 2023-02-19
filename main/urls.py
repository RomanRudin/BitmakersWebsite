from django.urls import path

from . import views

'''

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('bits/', views.bits, name='bits'),
    path('releases/', views.releases, name='releases'),
    path('links/', views.links, name='links'),
]