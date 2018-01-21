from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.spotify import Spotify
from home.models import User, Artist, Likeship, Dislikeship
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
    artist_id = User.objects.get(spotify_id=spot.user_id()).current_artist.spotify_id
    artist = get_object_or_404(Artist, pk=artist_id)
    return redirect('/artists/'+artist_id)

def liked(request):
    usr = User.objects.get(spotify_id=spot.user_id())
    Likeship.objects.create(user=usr, artist=usr.current_artist)
    new_id = spot.get_next_artist(usr.current_artist.spotify_id,True)
    artist = Artist.objects.create(spotify_id=new_id)
    usr.current_artist = artist
    usr.save()
    return redirect('/artists/'+new_id)

def disliked(request):
    usr = User.objects.get(spotify_id=spot.user_id())
    Dislikeship.objects.create(user=usr, artist=usr.current_artist)
    new_id = spot.get_next_artist(usr.current_artist.spotify_id,False)
    artist = Artist.objects.create(spotify_id=new_id)
    usr.current_artist = artist
    usr.save()
    return redirect('/artists/'+new_id)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'home/detail.html', {'artist': artist, 'image': spot.artist_image_url(artist_id), 'song': spot.artist_song_url(artist_id), 'name': spot.artist_name(artist_id)})
