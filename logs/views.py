from rest_framework import viewsets

from logs.models import ExceptionLog
from logs.serializers import ExceptionLogSerializer


class ExceptionLogViewSet(viewsets.ModelViewSet):
    """
    ExceptionLog API endpoint.
    """

    queryset = ExceptionLog.objects.all()
    serializer_class = ExceptionLogSerializer
