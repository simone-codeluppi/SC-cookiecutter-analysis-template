"""
Set utils to control logging in htcondor and dask
"""
from typing import *
import logging
import time
from pathlib import Path
from _constants import logger_settings


def init_logger():
    logging.root.handlers = []
    log_path = Path(logger_settings.logs_path.value)
    logging.captureWarnings(True)
    date_tag = time.strftime("%y%m%d_%H_%M_%S")
    fname = log_path / (date_tag + "_run.log")

    # Configure the fields to include in the JSON output. message is the main log string itself
    format_str = "%(asctime)s - %(module)s - %(levelname)-4s - %(lineno)d - %(message)s"
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

    # Normally we would attach the handler to the root logger, and this would be unnecessary
    # logger.propagate = True
    logger.debug("Created logger")
    return logger



# import logging
# from logging import config

# log_config = {
#     "version":1,
#     "root":{
#         "handlers" : ["console", "file"],
#         "level": "DEBUG"
#     },
#     "handlers":{
#         "console":{
#             "formatter": "std_out",
#             "class": "logging.StreamHandler",
#             "level": "DEBUG"
#         },
#         "file":{
#             "formatter":"std_out",
#             "class":"logging.FileHandler",
#             "level":"INFO",
#             "filename":"all_messages.log"
#         }
#     },
#     "formatters":{
#         "std_out": {
#             "format": "%(levelname)s : %(module)s : %(funcName)s : %(message)s",
#         }
#     },
# }

# config.dictConfig(log_config)


# [loggers]
# keys=root

# [handlers]
# keys=console, file

# [formatters]
# keys=std_out

# [logger_root]
# handlers = console, file
# level = DEBUG

# [handler_console]
# class = logging.StreamHandler
# level = DEBUG
# formatter = std_out


# [handler_file]
# class = logging.FileHandler
# kwargs = {"filename": "all_messages_conf.log"}
# level = INFO
# formatter = std_out

# [formatter_std_out]
# format = %(levelname)s : %(name)s : %(module)s : %(funcName)s : %(message)s