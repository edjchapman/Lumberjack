import collections


def group_logs(logs):
    """Group logs by project, appenv, app_location and subject.

    Join log values into a string using %SEP% as a separator
    to be counted combined then split into a dict for display in the notification.

    :param logs: QuerySet, ExceptionLog.
    :return: List, exception counts e.g. {"project": "w", "appenv": "x", "app_location": "y", "subject": "z", count: 3}
    """
    values_list = logs.values_list("project_name", "appenv", "app_location", "subject")
    joined_logs = ["%SEP%".join(i) for i in values_list]
    count_dict = dict(collections.Counter(joined_logs))
    split_tuples = [
        (k.split("%SEP%"), v) for k, v in count_dict.items()
    ]  # [([env, loc, subj], count), ...]
    display_dict = [
        {
            "project": lg[0],
            "appenv": lg[1],
            "app_location": lg[2],
            "subject": lg[3],
            "count": count,
        }
        for lg, count in split_tuples
    ]
    return display_dict
