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
        self.subscribers_count = int(self.channel['items'][0]['statistics']['subscriberCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.__youtube

    def to_json(self, name):
        with open(name, 'w', encoding='utf-8') as outfile:
            json.dump(self.channel, outfile, indent=2, ensure_ascii=False)

    def __str__(self):
        """Возвращает строковое представление объекта Channel в формате "<название_канала> (<ссылка_на_канал>)"."""
        return f'{self.title} ({self.url})'  # <название_канала> (<ссылка_на_канал>)

    def __add__(self, other):
        """Возвращает сумму числа подписчиков текущего объекта и переданного объекта `other`."""
        return int(self.followers) + int(other.followers)

    def __sub__(self, other):
        """Возвращает разность числа подписчиков текущего объекта и переданного объекта `other`."""
        return int(self.followers) - int(other.followers)

    def __ge__(self, other):
        """Возвращает `True`, если число подписчиков текущего объекта больше или равно числу подписчиков
        переданного объекта `other`, иначе `False`."""
        return int(self.followers) >= int(other.followers)

    def __eq__(self, other):
        """Возвращает `True`, если число подписчиков текущего объекта равно числу подписчиков переданного объекта
        `other`, иначе `False`. Если объект `other` не является экземпляром класса `Channel`, выбрасывается
        исключение типа `TypeError`. """
        self.__verify_classes(other)
        return self.__subscribers_count == other.__subscribers_count

    def __le__(self, other) -> bool:
        """Возвращает `True`, если число подписчиков текущего объекта меньше или равно числу подписчиков переданного
        объекта `other`, иначе `False`. Если объект `other` не является экземпляром класса `Channel`,
        выбрасывается исключение типа `TypeError`."""
        self.__verify_classes(other)
        return self.__subscribers_count <= other.__subscribers_count

    def __gt__(self, other):
        """Возвращает `True`, если число подписчиков текущего объекта больше числа подписчиков переданного
        объекта `other`, иначе `False`. Если объект `other` не является экземпляром класса `Channel`,
        выбрасывается исключение типа `TypeError`."""
        self.__verify_classes(other)
        return self.__subscribers_count > other.__subscribers_count

    @classmethod
    def __verify_classes(cls, other):
        """Проверяет, является ли объект `other` экземпляром класса `Channel`. Если объект не является экземпляром
        класса `Channel`, выбрасывается исключение типа `TypeError`."""
        if not isinstance(other, Channel):
            raise TypeError("Действие допустимо только для экземпляров класса Chanel")

    @property
    def subscribers_count(self):
        return self.subscribers_count

    @subscribers_count.setter
    def subscribers_count(self, value):
        self.__subscribers_count = value
