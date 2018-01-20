from django.shortcuts import render
from django.http import HttpResponse
from home.spotify import Spotify
from artists.models import User

# Create your views here.
spot = Spotify()

def index(request):
    auth_url = spot.get_auth_url()
    # if auth_url:
    #     htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    # else:
    #     htmlLoginButton = """
    #     <p>you're already logged into spotify</p>
    #     <p><a href='http://localhost:8000/my_info/'>my_info</a></p>
    #     <p><a href='http://localhost:8000/my_songs/'>my_songs</a></p>
    #     """
    return render(request, 'home/index.html', {'auth_url': auth_url})

def auth_page(request):
    spot.auth(request.get_full_path())
    User.objects.create(spotify_id=spot.user_id())
    return render(request, 'home/index.html') #{'auth_url': auth_url}) #HttpResponse("should be logged in")

def my_info(request):
    info = spot.user_info()
    return HttpResponse(repr(info))

def my_songs(request):
    songs = spot.user_songs()
    return HttpResponse(songs)
