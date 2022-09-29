from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.


def pavan(request):
    return HttpResponse('<h1>this is pavan</h1>')


def loki(request):
    return HttpResponse('<h2><marquee>he is my brother</marquee></h2>')


def siva(request):
    return HttpResponse('<i> siva is my best frnd </i>')


def harshadsir(request):
    return HttpResponse('<h3><marquee><i>harshadsir is my python teach</i></marquee></h3>')
