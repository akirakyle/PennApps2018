from django.db import models

class Artist(models.Model):
    spotify_id = models.CharField(max_length=64, primary_key=True)

class User(models.Model):
    spotify_id = models.CharField(max_length=64, primary_key=True, default='')
    liked = models.ManyToManyField(Artist, through='Likeship', related_name='likers', blank=True)
    disliked = models.ManyToManyField(Artist, through='Dislikeship', related_name='dislikers', blank=True)
    playlist_id = models.CharField(max_length=64, primary_key=False, default='')
    current_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Likeship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Dislikeship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
