import requests
import os



class Video:
    """
    Класс, представляющий видео на YouTube.

    Args:
    video_id (str): идентификатор видео на YouTube

    Attributes:
    video_id (str): идентификатор видео на YouTube
    title (str): заголовок видео
    link (str): ссылка на видео
    views (int): количество просмотров видео
    likes (int): количество лайков видео

    Methods:
    _get_video_data(self): Получает данные о видео с помощью YouTube Data API.
    __str__(self): Возвращает строковое представление видео.
    """

    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None
        self.link = None
        self.views = None
        self.likes = None
        self._get_video_data()

    def _get_video_data(self):
        """Данный метод используется для получения данных о видео с помощью YouTube Data API. Он делает запрос к API
        с использованием `video_id` и сохраняет полученные данные, такие как заголовок видео, ссылка на видео,
        количество просмотров и количество лайков. Если видео не найдено, метод выведет сообщение об ошибке."""

        __api_key: str = os.getenv('YT_API_KEY')
        api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2Cstatistics&id={self.video_id}&key={__api_key}"
        response = requests.get(api_url)
        data = response.json()
        if "items" in data:
            video_data = data["items"][0]
            self.title = video_data["snippet"]["title"]
            self.link = f"https://www.youtube.com/watch?v={self.video_id}"
            self.views = int(video_data["statistics"]["viewCount"])
            self.likes = int(video_data["statistics"]["likeCount"])
        else:
            print(f"Video with ID {self.video_id} not found.")

    def __str__(self):
        return f'{self.title}'     # <название_канала> (<ссылка_на_канал>)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        """
        Инициализирует экземпляр класса `PLVideo`.

        Args:
        -----
        video_id : str
            Идентификатор видео.
        playlist_id : str
            Идентификатор плейлиста, к которому принадлежит видео.
        """
        super().__init__(video_id)
        self.video_id = video_id
        self.playlist_id = playlist_id
        self.title = None
        self.link = None
        self.views = None
        self.likes = None
        super()._get_video_data()

