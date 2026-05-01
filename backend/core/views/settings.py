from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import SiteSettings
from core.serializers import SiteSettingsSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def site_settings(request):
    """
    GET /api/settings/

    Return the singleton SiteSettings row.
    """
    instance   = SiteSettings.load()
    serializer = SiteSettingsSerializer(instance)
    return Response(serializer.data)