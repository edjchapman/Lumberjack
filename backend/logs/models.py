import logging

from django.db import models


class LogLevels(models.IntegerChoices):
    NOTSET = logging.NOTSET, "Not Set"
    INFO = logging.INFO, "Info"
    WARNING = logging.WARNING, "Warning"
    DEBUG = logging.DEBUG, "Debug"
    ERROR = logging.ERROR, "Error"
    FATAL = logging.FATAL, "Fatal"


class ExceptionLog(models.Model):
    """
    Represents a message written to the logger.
    """

    project_name = models.CharField(max_length=100, db_index=True)
    appenv = models.CharField(max_length=100, db_index=True)
    app_location = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField()
    level = models.IntegerField(
        choices=LogLevels.choices, default=LogLevels.ERROR, db_index=True
    )
    subject = models.CharField(max_length=200)
    logger_name = models.CharField(max_length=100)
    path_name = models.CharField(max_length=200)
    func_name = models.CharField(max_length=100)
    line_num = models.IntegerField()
    traceback = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
