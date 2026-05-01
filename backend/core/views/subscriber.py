from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.models import Subscriber
from core.serializers import SubscriberSerializer


class SubscriberView(generics.CreateAPIView):
    """
    POST /api/subscribe/

    Add an email (and optional phone) to the mailing list.
    Duplicate-email validation is handled inside SubscriberSerializer.
    """

    queryset           = Subscriber.objects.all()
    serializer_class   = SubscriberSerializer
    permission_classes = [AllowAny]