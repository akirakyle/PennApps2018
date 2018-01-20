from django.conf import settings
from django.shortcuts import redirect
from spotipy import oauth2

import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = '1282047911'

class Spotify:
    def __init__(self):
        client_id=settings.SPOTIPY_CLIENT_ID
        client_secret=settings.SPOTIPY_CLIENT_SECRET
        redirect_uri=settings.SPOTIPY_REDIRECT_URI

        cache_path = ".cache-" + username
        self.sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret,
                                            redirect_uri, scope=scope,
                                            cache_path=cache_path)

    def get_auth_url(self):
        # try to get a valid token for this user, from the cache,
        # if not in the cache, the create a new (this will send
        # the user to a web page where they can authorize this app)

        token_info = self.sp_oauth.get_cached_token()

        if not token_info:
            auth_url = self.sp_oauth.get_authorize_url()
            #print(auth_url)
            return auth_url
        else:
            self.print_stuff(token_info)

    def auth(self, url):
        code = self.sp_oauth.parse_response_code(url)
        token_info = self.sp_oauth.get_access_token(code)
        self.print_stuff(token_info)

    def print_stuff(self, token_info):
        print(token_info)
        if token_info['access_token']:
            print("Access token available! Trying to get user information...")
            sp = spotipy.Spotify(token_info['access_token'])
            results = sp.current_user()
            print(results)

            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])
        else:
            print("Can't get token for", username)
