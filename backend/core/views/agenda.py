from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import AgendaItem
from core.serializers import AgendaItemSerializer


class AgendaItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List / retrieve YR27 agenda items.
    Pagination disabled — all active items are returned at once.
    """

    queryset           = AgendaItem.objects.filter(is_active=True)
    serializer_class   = AgendaItemSerializer
    permission_classes = [AllowAny]
    pagination_class   = None
    lookup_field       = 'slug'