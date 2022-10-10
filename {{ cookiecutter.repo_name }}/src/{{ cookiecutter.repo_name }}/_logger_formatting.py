"""
Set utils to control logging in htcondor and dask
"""
from typing import *
import logging
import time
from pathlib import Path
from _constants import logger_settings


def init_logger():
    # logging.root.handlers = []
    log_path = Path(logger_settings.logs_path.value)
    logging.captureWarnings(True)
    date_tag = time.strftime("%y%m%d_%H_%M_%S")
    fname = log_path / (date_tag + "_run.log")

    format_str = "%(asctime)s - level:%(levelname)-4s - module:%(module)s - function:%(funcName)s - line:%(lineno)d - message:%(message)s"
    formatter = logging.Formatter(fmt=format_str)

    # Create one file and one stream handler
    file_handler = logging.FileHandler(str(fname))  # Or FileHandler or anything else
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logger_settings.logs_level.value)

    return logger
