from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from core.models import Event
from core.serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = Event.objects.all()
    serializer_class   = EventSerializer
    permission_classes = [AllowAny]
    filter_backends    = [DjangoFilterBackend, SearchFilter]
    filterset_fields   = ['status', 'county', 'is_featured']
    search_fields      = ['title', 'venue']
    lookup_field       = 'slug'

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        qs         = self.queryset.filter(status='upcoming')[:6]
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)