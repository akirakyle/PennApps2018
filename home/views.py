from django.shortcuts import render
from django.http import HttpResponse
from home.spotify import Spotify
from artists.models import User

spot = Spotify()

def index(request):
    auth_url = spot.get_auth_url()
    return render(request, 'home/index.html', {'auth_url': auth_url})

def auth_page(request):
    spot.auth(request.get_full_path())
    try:
        User.objects.get(spotify_id=spot.user_id())
    except User.DoesNotExist:
        User.objects.create(spotify_id=spot.user_id())
    return render(request, 'home/index.html')

def do_the_thing(request):
    #stuff = spot.user_info()
    #stuff = spot.user_songs()
    #stuff = spot.user_top_artists()
    #stuff = spot.related_artist(spot.user_top_artists())
    #stuff = spot.artist_top_track(spot.user_top_artists())
    #stuff = spot.artist_image_url(spot.user_top_artists())
    stuff = spot.artist_song_url(spot.user_top_artists())
    #spot.test_add_artists()
    #stuff = spot.get_next_artist()
    return HttpResponse(stuff)
