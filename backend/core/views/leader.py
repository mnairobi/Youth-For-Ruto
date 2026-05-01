from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from core.models import Leader
from core.serializers import LeaderSerializer


class LeaderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List / retrieve YR27 leaders.

    Extra actions
    ─────────────
    GET /api/leaders/national/    → national-level leaders only
    GET /api/leaders/county_level/   → county-level leaders only
    GET /api/leaders/grassroots/  → grassroots-level leaders only
    """

    queryset           = Leader.objects.filter(is_active=True)
    serializer_class   = LeaderSerializer
    permission_classes = [AllowAny]
    pagination_class   = None
    filter_backends    = [DjangoFilterBackend, SearchFilter]
    filterset_fields   = ['level', 'position', 'county']
    search_fields      = ['full_name', 'custom_title']

    # ── Custom list actions ───────────────────────────────────────

    @action(detail=False, methods=['get'])
    def national(self, request):
        """Return only national-level leaders ordered by their display order."""
        qs         = self.queryset.filter(level='national')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def county_level(self, request):
        """Return only county-level leaders."""
        qs         = self.queryset.filter(level='county')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def grassroots(self, request):
        """Return only grassroots-level leaders."""
        qs         = self.queryset.filter(level='grassroots')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)