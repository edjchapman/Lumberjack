import json
import os

from logs.models import ExceptionLog


def setup_exception_logs():
    """
    Load fixtures from JSON file and save to ExceptionLog table.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "exceptionlog_fixtures.json")) as f:
        data = json.load(f)
        for i in data:
            ExceptionLog.objects.create(
                project_name=i.get("project_name"),
                appenv=i.get("appenv"),
                app_location=i.get("app_location"),
                created_at=i.get("created_at"),
                level=i.get("level"),
                subject=i.get("subject"),
                logger_name=i.get("logger_name"),
                path_name=i.get("path_name"),
                func_name=i.get("func_name"),
                line_num=i.get("line_num"),
                traceback=i.get("traceback"),
            )
