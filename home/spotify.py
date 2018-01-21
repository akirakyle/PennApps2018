from django.conf import settings
import spotipy
from spotipy import oauth2
from home.models import User, Artist, Likeship, Dislikeship
from django.db import IntegrityError

class Spotify:
    def __init__(self):
        scope = 'user-library-read user-top-read'
        cache = '.spotipyoauthcache'

        client_id=settings.SPOTIPY_CLIENT_ID
        client_secret=settings.SPOTIPY_CLIENT_SECRET
        redirect_uri=settings.SPOTIPY_REDIRECT_URI

        self.sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret,
                                            redirect_uri, scope=scope,
                                            cache_path=cache)

    def get_auth_url(self):
        # try to get a valid token for this user, from the cache,
        # if not in the cache, the create a new (this will send
        # the user to a web page where they can authorize this app)
        token_info = self.sp_oauth.get_cached_token()

        if token_info:
            self.sp = spotipy.Spotify(token_info['access_token'])
            #print(token_info['access_token'])
        else:
            return self.sp_oauth.get_authorize_url()

    def auth(self, url):
        code = self.sp_oauth.parse_response_code(url)
        token_info = self.sp_oauth.get_access_token(code)
        if token_info['access_token']:
            self.sp = spotipy.Spotify(token_info['access_token'])
            return True

    def user_info(self):
        return repr(self.sp.current_user())

    def user_id(self):
        return self.sp.current_user()['id']

    def user_songs(self):
        results = self.sp.current_user_saved_tracks()
        str = ''
        for item in results['items']:
            track = item['track']
            str += '<p>' + track['name'] + ' - ' + track['artists'][0]['name'] + '</p>'
        return str

    def user_top_artists(self,i=0):
        result = self.sp.current_user_top_artists(limit=30, offset=0, time_range='long_term')
        return result['items'][i]['id']

    def test_add_artists(self):
        usr = User.objects.get(spotify_id=self.user_id())
        for i in range(10):
            sid = self.user_top_artists(i)
            print(sid)
            try:
                artist = Artist.objects.create(spotify_id=sid)
                Likeship.objects.create(user=usr, artist=artist)
            except IntegrityError:
                pass
        for i in range(10,20):
            sid = self.user_top_artists(i)
            print(sid)
            try:
                artist = Artist.objects.create(spotify_id=sid)
                Dislikeship.objects.create(user=usr, artist=artist)
            except IntegrityError:
                pass

    def related_artists(self, artist_id):
        result = self.sp.artist_related_artists(artist_id)
        artists = []
        for i in range(len(result['artists'])):
            artists.append(result['artists'][i]['id'])
        return artists

    def artist_top_track(self, artist_id):
        result = self.sp.artist_top_tracks(artist_id)
        return result['tracks'][0]['name']

    def artist_image_url(self, artist_id):
        result = self.sp.artists([artist_id])
        return result['artists'][0]['images'][0]['url']

    def artist_song_url(self, artist_id):
        result = self.sp.artist_top_tracks(artist_id)
        return result['tracks'][0]['preview_url']

    def artist_name(self, artist_id):
        result = self.sp.artists([artist_id])
        return result['artists'][0]['name']

    def get_next_artist(self, artist_id):
        usr = User.objects.get(spotify_id=self.user_id())
        likes = Likeship.objects.filter(user=usr)
        print(likes)
        dislikes = Dislikeship.objects.filter(user=usr)
        print(dislikes)
        artists = likes.union(dislikes).order_by('date')[:20]
        print(artists)
        nlikes = artists.intersection(likes).count()
        print(nlikes)
        if nlikes/artists.count():
            new_artists = related_artist(artist_id)
            for new_id in new_artists:
                if (not Likeship.objects.filter(artist_id=new_id).exists() or
                    not Dislikeship.objects.filter(artist_id=new_id).exists()):
                    break
            else:
                get_next_artist()
