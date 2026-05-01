from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from core.models import NewsCategory, NewsArticle
from core.serializers import (
    NewsCategorySerializer,
    NewsListSerializer,
    NewsDetailSerializer,
)


class NewsCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """List all news categories (no pagination)."""

    queryset           = NewsCategory.objects.all()
    serializer_class   = NewsCategorySerializer
    permission_classes = [AllowAny]
    pagination_class   = None


class NewsArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List / retrieve published news articles.

    Filtering  : ?category=<id>  ?is_featured=true
    Search     : ?search=<term>  (title, excerpt, content)
    Ordering   : ?ordering=views  ?ordering=-created_at

    Extra actions
    ─────────────
    GET /api/news/featured/  → up to 6 featured articles
    GET /api/news/latest/    → the 6 most-recent articles
    """

    queryset           = NewsArticle.objects.filter(is_published=True)
    permission_classes = [AllowAny]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['category', 'is_featured']
    search_fields      = ['title', 'excerpt', 'content']
    ordering_fields    = ['created_at', 'views']
    lookup_field       = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NewsDetailSerializer
        return NewsListSerializer

    def retrieve(self, request, *args, **kwargs):
        """Increment view counter every time an article is opened."""
        instance        = self.get_object()
        instance.views += 1
        instance.save(update_fields=['views'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # ── Custom list actions ───────────────────────────────────────

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Return up to 6 featured articles."""
        qs         = self.queryset.filter(is_featured=True)[:6]
        serializer = NewsListSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Return the 6 most-recently published articles."""
        qs         = self.queryset[:6]
        serializer = NewsListSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)