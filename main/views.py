from multiprocessing import context
from pydoc import describe
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
import logging

from .models import Links, Beats, News, Tracks

def index(request) -> HttpResponse:
    return render(request, 'main/main.html')


def beats(request) -> HttpResponse:
    try:
        beats = Beats.objects.order_by('name') #TODO order_by('date')
    except Beats.DoesNotExist:
        raise Http404("Music does not exist")
    else:
        context = {
            'beats': beats,
        }
        return render(request, 'main/beats.html', context)
        

def tracks(request) -> HttpResponse:
    try:
        tracks = Tracks.objects.order_by('name') #TODO order_by('date')
    except Tracks.DoesNotExist:
        raise Http404("Music does not exist")
    else:
        context = {
            'tracks': tracks,
        }
        return render(request, 'main/tracks.html', context)


def releases(request) -> HttpResponse:
    try:
        news = News.objects.order_by('name')
    except News.DoesNotExist:
        raise Http404('News does not exist')
    else:
        context = {
            'news': news,
        }
        return render(request, 'main/releases.html', context)


def links(request) -> HttpResponse:
    try:
        links = Links.objects.order_by('name')
    except News.DoesNotExist:
        raise Http404('News does not exist')
    else:
        context = {
            'links': links,
        }
        return render(request, 'main/links.html', context)