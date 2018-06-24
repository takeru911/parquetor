import pandas as pd
import logging
from parquetor import logger
from enum import Enum

logger = logger.get_logger(__name__, logging.DEBUG)


class Reader(object):

    @classmethod
    def read(cls, file_path, mode=None):

        if mode is None:
            mode = cls._determine_file_read_mode(file_path)
        logger.info("read mode: {}".format(mode))
        if mode == Reader.Mode.CSV:
            return cls.read_csv(file_path)
        elif mode == Reader.Mode.JSON:
            return cls.read_json(file_path)

    @classmethod
    def _determine_file_read_mode(cls, file_path):

        split_list = file_path.split(".")
        estimate_file_ext = split_list[-1]
        logger.info("estimated file extension: {}".format(estimate_file_ext))
        if "csv" in estimate_file_ext:
            return Reader.Mode.CSV
        elif "json" in estimate_file_ext:
            return Reader.Mode.JSON

    @classmethod
    def read_csv(cls, file_path, na_values=['', 'N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN',
                                            '-nan', '1.#IND', '1.#QNAN', 'N/A', 'NA', 'NULL', 'NaN', 'n/a',
                                            'nan', 'null'],
                 compression="infer", sep=",", delimiter=" "):
        data = pd.read_csv(file_path, na_values=na_values, compression=compression, sep=sep, delimiter=delimiter)
        logger.info("{} (format: csv) loaded".format(file_path))

        return data

    @classmethod
    def read_json(cls, file_path, compression="infer", lines=True):
        data = pd.read_json(file_path, compression=compression, lines=lines)
        logger.info("{} (format: json) loaded".format(file_path))

        return data

    class Mode(Enum):
        CSV = 1
        JSON = 2
