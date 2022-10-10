"""
Set utils to control logging in htcondor and dask
"""
from typing import *
import logging
import time
from pathlib import Path
from logging import Logger


def formatted_logger(log_path: str = "../../logs/", logging_level: str = "DEBUG") -> Logger:
    """Formatted logger that save stream output in console and save to file.

    Args:
        log_path (str): path where to save the log file
        logging_level (str): selected level for logging ex. 'DEBUG'

    Returns:
        logger (logger)
    """

    log_path = Path(log_path)
    logging.captureWarnings(True)
    date_tag = time.strftime("%y%m%d_%H_%M_%S")
    fname = log_path / (date_tag + "_run.log")

    # Configure the fields to include in the JSON output. message is the main log string itself
    format_str = "%(asctime)s - %(name)s - %(levelname)-4s - %(message)s"
    formatter = logging.Formatter(fmt=format_str)
    
    # Create one file and one stream handler
    file_handler = logging.FileHandler(str(fname))  # Or FileHandler or anything else
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging_level)

    # Normally we would attach the handler to the root logger, and this would be unnecessary
    logger.propagate = True
    logger.debug("Created logger")
    return logger
