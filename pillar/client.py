from datetime import datetime
from typing import List

import requests


class Pillar:
    '''
    Base API Class. Import with: 

    ```
    from pillar import Pillar
    ```
    '''

    def __init__(self, token=None, base_url="") -> None:
        '''
        Initialization function for the class.

        The variable `token` is the API token needed for the API itself. The variable `base_url` is the url
        base URL for the API.
        '''
        if token is None:
            raise AssertionError('No token specified.')

        self.base_url = base_url
        self.token = token
        self.payload = {}

        self.response = None

    def get_streamers_to_poll(self) -> List[str]:
        '''
        Gets the streamers that the application should check for. Returns a list.
        '''
        self.payload = {
            'server_token': self.token
        }

        self.response = requests.post(
            f'{self.base_url}/getStreamsToPoll', json=self.payload)
        self.response.raise_for_status()
        return self.response.json()

    def post_video(self, twitch_username, thumbnail_url, video_url, video_title) -> None:
        '''
        Posts the video to the database. All input variables are strings and are self explanatory.
        '''
        self.payload = {
            'server_token': self.token,
            'twitch_username': twitch_username,
            'thumbnail_url': thumbnail_url,
            'video_url': video_url,
            'video_title': video_title,
            'timestamp': datetime.now()
        }

        self.response = requests.post(
            f'{self.base_url}/postUserVideo', json=self.payload)
        self.response.raise_for_status()

    def get_youtube_credentials(self, twitch_username) -> dict:
        '''
        Gets the YouTube credentials for the user.
        '''
        self.payload = {
            'server_token': self.token,
            'twitch_username': twitch_username
        }

        self.response = requests.post(
            f'{self.base_url}/youtube/getUserYTToken', json=self.payload)
        self.response.raise_for_status()
        return self.response.json()
