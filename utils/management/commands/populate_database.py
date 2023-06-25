from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from logs.tests.factories.exception_logs import setup_exception_logs


class Command(BaseCommand):
    help = "Populate database using data factories in apps"

    def handle(self, *args, **options):
        self.setup_test_user()
        setup_exception_logs()

    @staticmethod
    def setup_test_user():
        try:
            _ = User.objects.get(username="testuser@lumberjacklogs.com")
        except User.DoesNotExist:
            u = User.objects.create_user(
                "testuser@lumberjacklogs.com", password="password"
            )
            u.is_superuser = True
            u.is_staff = True
            u.save()
