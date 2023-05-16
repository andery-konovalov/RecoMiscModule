import logging
from logging.config import dictConfig

SERVER_LOGGER = "server_logger"
CONSOLE_LOGGER = "console_logger"
ACCESS_LOGGER = "access_logger"
ERROR_LOGGER = "error_logger"


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
            "ERROR_HANDLER": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "default",
                "level": logging.INFO,
                "filename": error_file,
                "maxBytes": file_rotation_max_bytes,
                "backupCount": 100
            },
            "ACCESS_HANDLER": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "default",
                "level": logging.INFO,
                "filename": access_file,
                "maxBytes": file_rotation_max_bytes,
                "backupCount": 100
            },
            "COMMON_HANDLER": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "for_file",
                "level": logging.INFO,
                "filename": server_log_file,
                "maxBytes": file_rotation_max_bytes,
                "backupCount": 100
            },
            "CONSOLE_HANDLER": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": logging.INFO,
                "stream": "ext://sys.stdout"
            }
        },
        "loggers": {
            SERVER_LOGGER: {
                "level": logging.INFO,
                "handlers": ["COMMON_HANDLER"],
                "propagate": False
            },
            ACCESS_LOGGER: {
                "level": logging.INFO,
                "handlers": ["ACCESS_HANDLER"],
                "propagate": False
            },
            ERROR_LOGGER: {
                "level": logging.INFO,
                "handlers": ["ERROR_HANDLER"],
                "propagate": False
            },
            CONSOLE_LOGGER: {
                "level": logging.INFO,
                "handlers": ["CONSOLE_HANDLER"],
                "propagate": False}
        }
    })


LOGGER = None
RABBIT_LOGGER = None
