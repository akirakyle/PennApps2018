from django.conf import settings

import spotipy
import spotipy.util as util

scope = 'user-library-read'

class Spotify:
    def __init__(self):
        username = '1282047911'
        token = util.prompt_for_user_token(username,scope,
                                            client_id=settings.SPOTIPY_CLIENT_ID,
                                            client_secret=settings.SPOTIPY_CLIENT_SECRET,
                                            redirect_uri=settings.SPOTIPY_REDIRECT_URI)
        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])
        else:
            print("Can't get token for", username)
