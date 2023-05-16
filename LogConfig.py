import logging
from logging.config import dictConfig

SERVER_LOGGER = "server_logger"
CONSOLE_LOGGER = "console_logger"
CHERRY_ACCESS_LOGGER = "CHERRY_ACCESS_LOGGER"
CHERRY_ERROR_LOGGER = "CHERRY_ERROR_LOGGER"


def set_logging(error_file, access_file, server_log_file):
    # sets up logging for the given name
    file_rotation_max_bytes = 1024 * 1000
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(message)s"},
            "for_file": {
                "format": "'%(asctime)s - %(message)s"
            }},
        "handlers": {
            "CHERRY_ERROR": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "default",
                "level": logging.INFO,
                "filename": error_file,
                "maxBytes": file_rotation_max_bytes,
                "backupCount": 100
            },
            "CHERRY_ACCESS": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "default",
                "level": logging.INFO,
                "filename": access_file,
                "maxBytes": file_rotation_max_bytes,
                "backupCount": 100
            },
            "SERVER_INFO": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "for_file",
                "level": logging.INFO,
                "filename": server_log_file,
                "maxBytes": file_rotation_max_bytes,
                "backupCount": 100
            },
            CONSOLE_LOGGER: {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": logging.INFO,
                "stream": "ext://sys.stdout"
            }
        },
        "loggers": {
            SERVER_LOGGER: {
                "level": logging.INFO,
                "handlers": ["SERVER_INFO"],
                "propagate": False
            },
            CHERRY_ACCESS_LOGGER: {
                "level": logging.INFO,
                "handlers": ["CHERRY_ACCESS"],
                "propagate": False
            },
            CHERRY_ERROR_LOGGER: {
                "level": logging.INFO,
                "handlers": ["CHERRY_ERROR"],
                "propagate": False
            },
            CONSOLE_LOGGER: {
                "level": logging.INFO,
                "handlers": [CONSOLE_LOGGER],
                "propagate": False}
        }
    })


LOGGER = None
RABBIT_LOGGER = None
