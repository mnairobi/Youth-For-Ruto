from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import Testimonial
from core.serializers import TestimonialSerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List / retrieve active testimonials.
    Pagination disabled — all items are returned at once.
    """

    queryset           = Testimonial.objects.filter(is_active=True)
    serializer_class   = TestimonialSerializer
    permission_classes = [AllowAny]
    pagination_class   = None