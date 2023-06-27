import logging

from celery import shared_task
from django.core.paginator import Paginator
from django.utils import timezone as tz

from logs.models import ExceptionLog

logger = logging.getLogger(__name__)


@shared_task
def purge_old_logs(older_than_days=14):
    """Cleanup old logs.  Paginated to avoid excessive memory use on large result sets.

    :param older_than_days: Int, number of days old the logs should be at least.
    """
    old_logs = ExceptionLog.objects.filter(
        created_at__lt=tz.localdate() - tz.timedelta(days=older_than_days)
    )
    paginator = Paginator(old_logs, 100)
    for page in paginator:
        logger.info(
            "Deleting old logs chunk {} of {}".format(page.number, paginator.num_pages)
        )
        for log in page.object_list:
            _ = log.delete()
