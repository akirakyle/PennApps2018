from django.shortcuts import render
from django.http import HttpResponse
from home.spotify import Spotify

# Create your views here.
spot = Spotify()

def index(request):
    auth_url = spot.get_auth_url()
    if auth_url:
        htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    else:
        htmlLoginButton = "you're already logged into spotify"
    return HttpResponse(htmlLoginButton)

def auth_page(request):
    print(request.get_full_path())
    spot.auth(request.get_full_path())
    return HttpResponse("should be logged in")
