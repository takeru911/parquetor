import sys
from logging import (
    getLogger,
    StreamHandler,
    INFO
)
from colorlog import ColoredFormatter


def get_logger(name, level=INFO):
    log_formatter = ColoredFormatter("%(log_color)s %(asctime)s %(levelname)s :%(message)s",
                                     reset=True,
                                     log_colors={'DEBUG': 'blue',
                                                 'INFO': 'green',
                                                 'WARNING': 'yellow',
                                                 'ERROR': 'red,bg_white',
                                                 'CRITICAL': 'red,bg_white', },
                                     secondary_log_colors={},
                                     style='%'
                                     )
    logger = getLogger(name)
    handler = StreamHandler(stream=sys.stdout)
    handler.setFormatter(log_formatter)
    handler.setLevel(INFO)
    logger.addHandler(handler)
    logger.setLevel(INFO)
    logger = getLogger(name)
    logger.setLevel(level)

    return logger
