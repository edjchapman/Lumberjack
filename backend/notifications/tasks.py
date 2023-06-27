from django.conf import settings
import logging

from celery import shared_task
from django.core.mail import send_mail
from django.template.defaultfilters import pluralize
from django.template.loader import render_to_string
from django.utils import timezone as tz

from logs.models import ExceptionLog
from notifications.utils import group_logs

logger = logging.getLogger(__name__)


@shared_task
def daily_summary():
    pass


@shared_task
def surge_alert(time_period=1, threshold=1):
    """Send alert email if exceptions exceed threshold for time period.

    :param time_period: INT, time period in minutes.
    :param threshold: INT, number of exceptions needed to trigger email.
    """
    logs = ExceptionLog.objects.filter(
        created_at__gte=tz.localtime() - tz.timedelta(minutes=time_period),
    )
    total_count = logs.count()
    if total_count > threshold:
        log_dicts = group_logs(logs)
        context = {
            "alert_time": tz.localtime().strftime("%c"),
            "total_count": total_count,
            "time_period": time_period,
            "log_dicts": log_dicts,
        }
        send_mail(
            subject="Surge Alert - More than {} exception{} in the last {} minute{}".format(
                total_count, pluralize(total_count), time_period, pluralize(time_period)
            ),
            message="",
            from_email="alerts@lumberjacklogs.com",
            html_message=render_to_string("surge_alert.html", context),
            recipient_list=settings.ALERT_RECIPIENTS,
        )
