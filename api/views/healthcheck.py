
from rest_framework.response import Response
from rest_framework.views import APIView

from lib.gen_logger import get_logger

LOGGER = get_logger(__name__)


class HealthcheckView(APIView):
    serializer_class = None

    def get(self, request, *args, **kwargs):
        LOGGER.info('healthcheck')
        return Response('healthy')
