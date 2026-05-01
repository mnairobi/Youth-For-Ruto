from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import (
    MemberRegistration,
    County,
    Event,
    Leader,
)


@api_view(['GET'])
@permission_classes([AllowAny])
def stats(request):
    """
    GET /api/stats/
    Returns real counts from the database.
    """
    data = {
        'total_members':  MemberRegistration.objects.count(),
        'total_counties': MemberRegistration.objects.values(
                              'county'
                          ).distinct().count(),
        'total_events':   Event.objects.count(),
        'total_leaders':  Leader.objects.filter(is_active=True).count(),
    }

    return Response(data)