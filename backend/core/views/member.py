from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.models import MemberRegistration
from core.serializers import MemberRegistrationSerializer


class MemberRegistrationView(generics.CreateAPIView):
    """
    POST /api/join/

    Register a new YR27 member.
    Validation (duplicate ID number, phone format) is handled
    inside MemberRegistrationSerializer.
    """

    queryset           = MemberRegistration.objects.all()
    serializer_class   = MemberRegistrationSerializer
    permission_classes = [AllowAny]