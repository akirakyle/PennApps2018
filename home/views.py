from django.shortcuts import render
from django.http import HttpResponse
from home.spotify import Spotify

spot = Spotify()

def index(request):
    auth_url = spot.get_auth_url()
    if auth_url:
        htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    else:
        htmlLoginButton = """
        <p>you're already logged into spotify</p>
        <p><a href='http://localhost:8000/my_info/'>my_info</a></p>
        <p><a href='http://localhost:8000/my_songs/'>my_songs</a></p>
        <p><a href='http://localhost:8000/my_artists/'>my_artists</a></p>
        """
    return HttpResponse(htmlLoginButton)

def auth_page(request):
    if spot.auth(request.get_full_path()):
        return HttpResponse("successfully logged in")
    else:
        return HttpResponse("something went wrong logging in")

def my_info(request):
    info = spot.user_info()
    return HttpResponse(info)

def my_songs(request):
    songs = spot.user_songs()
    return HttpResponse(songs)

def my_top_artists(request):
    artists = spot.user_top_artists()
    return HttpResponse(artists)
