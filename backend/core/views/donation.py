from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.models import Donation
from core.serializers import DonationSerializer


class DonationView(generics.CreateAPIView):
    """
    POST /api/donate/

    Record a donation pledge.
    Payment status is updated externally (M-Pesa callback, manual admin update).
    """

    queryset           = Donation.objects.all()
    serializer_class   = DonationSerializer
    permission_classes = [AllowAny]