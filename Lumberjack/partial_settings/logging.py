import os

from .vars import BASE_DIR

LOG_DIR = BASE_DIR / "logfiles"

os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "logfile": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "verbose",
            "filename": LOG_DIR / "info_logfile.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "logfile"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console", "logfile"],
            "level": "ERROR",
            "propagate": False,
        },
        "": {
            "handlers": ["console", "logfile"],
            "level": "INFO",
        },
    },
}
