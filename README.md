# PennApps2018

## Installation
Requires python 3. Install required python dependencies using requirements.txt
```bash
pip install -r requirements.txt
```
Install PostgreSQL ([guide here for macOS](https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb)), and create a user named admin

You'll need to create a `.env` file in the PennApps2018 folder with the following info

```
DEBUG=True
SECRET_KEY=somethingrandom
DATABASE_URL=postgres://admin:password@localhost/pennapps
ALLOWED_HOSTS=.localhost
SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=
SPOTIPY_REDIRECT_URI=http://localhost:8000/auth/
```
Where the spotipy info you get from signing up for the [spotify API](developer.spotify.com/dashboard/applications)

You can run the app locally with `python manage.py runserver`. To reset the database `python manage.py flush` and to reset the cached login credentials delete `.spotipyoauthcache`

## Inspiration

Although Spotify has many premade playlists, these are usually based on one thing, whether it be the artist, genre, era, or mood. Playlists that took more than one of these into consideration are rare, and most likely created by hand. This, we wanted to create a way for an app/algorithm to create these types of playlists with ease.

## What it does

Sonicswype is a tinder-inspired webapp that plays a snippet of a track to the user. Then, the user swipes left or right depending if they like the track. The next track is decided by using Spotify’s related artist function. Liked tracks are ultimately stored in a Spotify playlist.

## How we built it

We built mostly using django and the spotipy library.

## Challenges we ran into

User authentication with OAuth and Spotify proved to be somewhat challenging. We also struggled with playlist generation and getting the database and views to play nicely with some of the edge cases of Spotify's API, such as artists without images.

## Accomplishments that we're proud of

Sometimes it doesn't crash. It makes a playlist right in the users' spotify.
What we learned

We weren't all familiar with Django or full-stack dev, so that was a biggie for some of us. We all learned a lot about the ins and outs of the Spotify API and creating a somewhat complex database structure for liked/disliked artists. We also learned about how to serve audio in HTML.

## What's next for sonicswype

The original vision of the webapp would have it not only create playlists where the user has explicitly selected the song, but could also automatically search for songs depending on the user’s previous swipes in the session. For example, if the user was swiping on slow, acoustic songs, the app would go to related artists and find songs that would have similar qualities using Spotify’s api classifications. Another feature would be to have the ability for the app to backtrack in its ‘finding’ of related artists and go to another related artist.

