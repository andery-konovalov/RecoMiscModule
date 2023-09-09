import logging
from logging.config import dictConfig

SERVER_LOGGER = "server_logger"
CONSOLE_LOGGER = "console_logger"


def set_logging(server_log_file, rabbit_consumer_log_file):
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
            "SERVER_HANDLER": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "for_file",
                "level": logging.INFO,
                "filename": server_log_file,
                "maxBytes": file_rotation_max_bytes,
                "backupCount": 100
            },
            "RABBIT_HANDLER": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "for_file",
                "level": logging.INFO,
                "filename": rabbit_consumer_log_file,
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
                "handlers": ["SERVER_HANDLER"],
                "propagate": False
            },
            "pika": {
                "level": logging.INFO,
                "handlers": ["RABBIT_HANDLER"],
                "propagate": False
            },
            CONSOLE_LOGGER: {
                "level": logging.INFO,
                "handlers": ["CONSOLE_HANDLER"],
                "propagate": False}
        },
        "root": {
            'level': logging.INFO,
            'handlers': ["SERVER_HANDLER", "CONSOLE_HANDLER", "RABBIT_HANDLER"]
        }
    })
