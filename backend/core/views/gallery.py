from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from core.models import GalleryCategory, GalleryImage
from core.serializers import GalleryCategorySerializer, GalleryImageSerializer


class GalleryCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """List all gallery categories (no pagination)."""

    queryset           = GalleryCategory.objects.all()
    serializer_class   = GalleryCategorySerializer
    permission_classes = [AllowAny]
    pagination_class   = None


class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List / retrieve gallery images.

    Filtering  : ?category=<id>  ?is_featured=true
    """

    queryset           = GalleryImage.objects.all()
    serializer_class   = GalleryImageSerializer
    permission_classes = [AllowAny]
    filter_backends    = [DjangoFilterBackend]
    filterset_fields   = ['category', 'is_featured']