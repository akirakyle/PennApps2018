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
Where the spotipy info you get from signing up for the [spotify API](https://developer.spotify.com/)

You can run the app locally with `python manage.py runserver`. To reset the database run `python manage.py flush` and to reset the cached login credentials delete `.spotipyoauthcache`

## What it does

Sonicswype is a tinder-inspired webapp that plays a snippet of a track to the user. Then, the user swipes left or right depending if they like the track. The next track is decided by using Spotify’s related artist function. Liked tracks are ultimately stored in a Spotify playlist.
