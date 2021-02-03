import os

import pytest

from pillar import Pillar

def test_initialization():
    token = os.environ.get('PILLAR_TOKEN')
    base_url = os.environ.get('PILLAR_BASE_URL')
    client = Pillar(token, base_url)

    assert token == client.token
    assert base_url == client.base_url


def test_get_streamers_to_poll():
    token = os.environ.get('PILLAR_TOKEN')
    base_url = os.environ.get('PILLAR_BASE_URL')
    client = Pillar(token, base_url)

    streamers = client.get_streamers_to_poll()
    
    assert streamers

def test_get_youtube_credentials():
    token = os.environ.get('PILLAR_TOKEN')
    base_url = os.environ.get('PILLAR_BASE_URL')
    client = Pillar(token, base_url)

    credentials = client.get_youtube_credentials(os.environ.get('TEST_STREAMER'))

    assert credentials

@pytest.mark.skip(reason="Need to figure out if test is broken or function is broken.")
def test_post_video():
    token = os.environ.get('PILLAR_TOKEN')
    base_url = os.environ.get('PILLAR_BASE_URL')
    client = Pillar(token, base_url)

    client.post_video(
        twitch_username=os.environ.get('TEST_STREAMER'), 
        thumbnail_url='https://github.com/pillargg/pillargg.github.io/raw/master/docs/pillargg.png',
        video_url='https://www.youtube.com/watch?v=vfQailtvIB4',
        video_title='Test Video')

    assert True