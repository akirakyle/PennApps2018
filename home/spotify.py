from django.conf import settings
import spotipy
from spotipy import oauth2

class Spotify:
    def __init__(self):
        scope = 'user-library-read'
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
        self.token_info = self.sp_oauth.get_cached_token()

        if not self.token_info:
            return self.sp_oauth.get_authorize_url()
        #else:
        #    self.print_stuff(token_info)

    def auth(self, url):
        code = self.sp_oauth.parse_response_code(url)
        self.token_info = self.sp_oauth.get_access_token(code)
        #self.print_stuff(token_info)

    def user_info(self):
        #print(self.token_info)
        if self.token_info['access_token']:
            print("Access token available! Trying to get user information...")
            sp = spotipy.Spotify(self.token_info['access_token'])
            results = sp.current_user()
            print(results)
            return results

        else:
            print("Can't get token")

    def user_songs(self):
        #print(token_info)
        if self.token_info['access_token']:
            print("Access token available! Trying to get user information...")
            sp = spotipy.Spotify(self.token_info['access_token'])
            results = sp.current_user_saved_tracks()
            str = ''
            for item in results['items']:
                track = item['track']
                str += '<p>' + track['name'] + ' - ' + track['artists'][0]['name'] + '</p>'
            return str
        else:
            print("Can't get token")
