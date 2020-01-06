import logging

from conf.settings import LOG_FORMAT, LOG_LEVEL, LOG_CONSOLE, LOG_FILE


class logman:
    """
    log module
    """
    def __init__(self, __logman=None):
        self.__logman = logging.getLogger(__logman)
        self.__logman.setLevel(LOG_LEVEL)
        formatter = logging.Formatter(LOG_FORMAT)

        file_handler = logging.FileHandler(LOG_FILE)
        stdo = logging.StreamHandler(LOG_CONSOLE)

        file_handler.setFormatter(formatter)
        stdo.setFormatter(formatter)

        if not self.__logman.handlers:
            self.__logman.addHandler(file_handler)
            self.__logman.addHandler(stdo)

    def getLog(self):
        return self.__logman
