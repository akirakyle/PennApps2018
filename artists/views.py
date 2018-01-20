from django.shortcuts import get_object_or_404, render

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return template.render(request, 'artists/detail.html', {'artist': artist})