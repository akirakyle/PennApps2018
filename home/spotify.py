from django.conf import settings
import spotipy
from spotipy import oauth2

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
            print(token_info['access_token'])
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

    def user_top_artists(self):
        result = self.sp.current_user_top_artists(limit=2, offset=0, time_range='long_term')
        return result['items'][0]['id']

    def related_artist(self, artist_id):
        result = self.sp.artist_related_artists(artist_id)
        print(result['artists'][0]['name'])
        return result['artists'][0]['name']
