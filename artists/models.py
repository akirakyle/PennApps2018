from django.db import models

class Artist(models.Model):
    spotify_id = models.CharField(max_length=64, primary_key=True)

class User(models.Model):
    spotify_id = models.CharField(max_length=64, primary_key=True, default='')
    liked = models.ManyToManyField(Artist, through='Likeship', related_name='likers', blank=True)
    disliked = models.ManyToManyField(Artist, through='Dislikeship', related_name='dislikers', blank=True)

class Likeship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    start_date = models.DateTimeField('date begun')

class Dislikeship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    start_date = models.DateTimeField('date begun')