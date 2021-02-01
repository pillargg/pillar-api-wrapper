from datetime import datetime

import requests


class Pillar:
    def __init__(self, token=None, base_url=""):

        if token is None:
            raise AssertionError('No token specified.')

        self.base_url = base_url
        self.token = token
        self.payload = {}

        self.response = None

    def get_streamers_to_poll(self):

        self.payload = {
            'server_token': self.token
        }

        self.response = requests.post(
            f'{self.base_url}/getStreamsToPoll', json=self.payload)
        self.response.raise_for_status()
        return self.response.json()

    def post_video(self, twitch_username, thumbnail_url, video_url, video_title):

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

    def get_youtube_credentials(self, twitch_username):

        self.payload = {
            'server_token': self.token,
            'twitch_username': twitch_username
        }

        self.response = requests.post(
            f'{self.base_url}/youtube/getUserYTToken', json=self.payload)
        self.response.raise_for_status()
        return self.response.json()
