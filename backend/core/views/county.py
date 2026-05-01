from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import County
from core.serializers import CountySerializer


class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve all 47 Kenyan counties.
    Pagination is disabled — the full list is always returned.
    """

    queryset           = County.objects.all()
    serializer_class   = CountySerializer
    permission_classes = [AllowAny]
    pagination_class   = None