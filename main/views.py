from multiprocessing import context
from pydoc import describe
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
import logging

from .models import Music

def index(request) -> HttpResponse:
    try:
        bit = Music.objects.order_by('name') #TODO order_by('date')
    except Music.DoesNotExist:
        raise Http404("Music does not exist")
    else:
        context = {
            'bit': bit,
        }
        return render(request, 'cv/main.html', context)