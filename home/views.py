from django.shortcuts import render
from django.http import HttpResponse
from home.spotify import Spotify
from home.models import User, Artist
from django.shortcuts import get_object_or_404

spot = Spotify()

def index(request):
    auth_url = spot.get_auth_url()
    return render(request, 'home/index.html', {'auth_url': auth_url})

def auth_page(request):
    spot.auth(request.get_full_path())
    if not User.objects.filter(spotify_id=spot.user_id()).exists():
        artist = Artist.objects.create(spotify_id=spot.user_top_artist())
        User.objects.create(spotify_id=spot.user_id(), current_artist=artist)
    return render(request, 'home/index.html')

def do_the_thing(request):
    #stuff = spot.user_info()
    #stuff = spot.user_songs()
    #stuff = spot.user_top_artist()
    #stuff = spot.artist_name(spot.user_top_artists())
    #stuff = spot.related_artists(spot.user_top_artists())
    #stuff = spot.artist_top_track(spot.user_top_artists())
    #stuff = spot.artist_image_url(spot.user_top_artists())
    #stuff = spot.artist_song_url(spot.user_top_artists())
    spot.test_add_artists()
    stuff = spot.artist_name(spot.get_next_artist(spot.user_top_artists()))

    #artist_id = User.objects.get(spotify_id=spot.user_id()).current_artist
    #print(artist_id)
    #artist = get_object_or_404(Artist, pk=artist_id)
    #return render(request, 'home/detail.html', {'artist': artist, 'image': spot.artist_image_url(artist_id), 'song': spot.artist_song_url(artist_id), 'name': spot.artist_name(artist_id)})
    return HttpResponse(stuff)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'home/detail.html', {'artist': artist, 'image': spot.artist_image_url(artist_id), 'song': spot.artist_song_url(artist_id), 'name': spot.artist_name(artist_id)})
