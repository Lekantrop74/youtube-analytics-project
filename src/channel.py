# from helper.youtube_api_manual import build, api_key
from googleapiclient.discovery import build
import json
import os



class Channel:
    """Класс для ютуб-канала"""
    __api_key: str = os.getenv('YT_API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = self.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id

        self.title = self.channel['items'][0]['snippet']['title']
        self.about = self.channel['items'][0]['snippet']['description']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.followers = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.views = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.__youtube

    def to_json(self, name):
        with open(name, 'w', encoding='utf-8') as outfile:
            json.dump(self.channel, outfile, indent=2, ensure_ascii=False)

    # @property
    # def channel_id(self) -> str:
    #     return self.__channel_id

    def __str__(self):
        return f'{self.title} ({self.url})'     # <название_канала> (<ссылка_на_канал>)

    def __add__(self, other):
        return int(self.followers) + int(other.followers)

    def __sub__(self, other):
        return int(self.followers) - int(other.followers)

    def __ge__(self, other):
        return int(self.followers) >= int(other.followers)

