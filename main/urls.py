from django.urls import path

from . import views

'''

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('beats/', views.beats, name='beats'),
    path('tracks/', views.tracks, name='tracks'),
    path('releases/', views.releases, name='releases'),
    path('links/', views.links, name='links'),
]