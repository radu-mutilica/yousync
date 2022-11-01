import logging


class YouSync:
    def __init__(self, config):
        self.__config = config

    def run(self):
        logging.info('starting new run')
        logging.info('finished run')
