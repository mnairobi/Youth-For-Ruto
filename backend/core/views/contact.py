from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.models import ContactMessage
from core.serializers import ContactMessageSerializer


class ContactMessageView(generics.CreateAPIView):
    """
    POST /api/contact/

    Accept an inbound contact / enquiry message.
    """

    queryset           = ContactMessage.objects.all()
    serializer_class   = ContactMessageSerializer
    permission_classes = [AllowAny]