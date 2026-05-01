from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import MemberRegistration, County, Event, Leader
from core.serializers import StatsSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def stats(request):
    """
    GET /api/stats/

    Return aggregated site-wide statistics displayed on the homepage counter.
    """
    data = {
        'total_members':    MemberRegistration.objects.count(),
        'total_counties':   County.objects.filter(registered_youth__gt=0).count() or 47,
        'total_events':     Event.objects.count(),
        'total_leaders':    Leader.objects.filter(is_active=True).count(),
        'total_mobilizers': MemberRegistration.objects.filter(
                                role_interest='mobilizer'
                            ).count(),
    }
    serializer = StatsSerializer(data)
    return Response(serializer.data)