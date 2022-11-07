import logging

from pyyoutube import Api

from core import helpers


class YouSync:
    def __init__(self, config):
        self.__config = config
        self.api = Api(access_token=config.YOUTUBE_ACCESS_TOKEN)
        self.last_run = helpers.get_last_run(path=config.SAVED_STATE_PATH)

    def run(self):
        logging.info('starting new run')

        videos = self.my_likes()
        for idx, item in enumerate(videos.items):
            title = sanitize(item.snippet)
            print(idx, title)

        logging.info('finished run')

    def my_likes(self):
        return self.api.get_videos_by_myrating(rating="like", count=35)


def sanitize(details):
    if '-' not in details.title and ' - Topic' in details.channelTitle:
        artist = details.channelTitle.replace(' - Topic', '')
        return '{} - {}'.format(artist, details.title)
    else:
        return details.title
