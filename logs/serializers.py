from rest_framework import serializers

from logs.models import ExceptionLog


class ExceptionLogSerializer(serializers.HyperlinkedModelSerializer):
    """
    ExceptionLog Serializer
    """

    class Meta:
        model = ExceptionLog
        fields = [
            "url",
            "project_name",
            "appenv",
            "app_location",
            "created_at",
            "level",
            "subject",
            "logger_name",
            "path_name",
            "func_name",
            "line_num",
            "traceback",
        ]
