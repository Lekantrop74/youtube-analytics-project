import requests
import os
import json
from datetime import timedelta, datetime
from src.video import PLVideo



class PlayList:
    def __init__(self, playlist_id):
        # self.playlist_id = playlist_id
        # self.__api_key: str = os.getenv('YT_API_KEY')
        # api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2Cstatistics&id={self.playlist_id}&key={ self.__api_key} "
        # response = requests.get(api_url)
        # self.data = response.json()

        self.playlist_id = playlist_id
        api_key = os.getenv('YT_API_KEY')

        url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_id}&key={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            self.data = response.json()
            # обработка полученных данных
