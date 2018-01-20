from django.shortcuts import render
from django.http import HttpResponse
from home.spotify import Spotify

# Create your views here.

def index(request):
    Spotify()
    return HttpResponse("Hello, world. You're at the polls index.")
