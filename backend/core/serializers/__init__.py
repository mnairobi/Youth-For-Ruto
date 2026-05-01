# ---------------------------------------------------------------------------
# core/serializers/__init__.py
#
# Re-export every serializer so that views.py (or views/) can still do:
#
#   from core.serializers import CountySerializer, LeaderSerializer, ...
#
# ---------------------------------------------------------------------------

from .county        import CountySerializer
from .leader        import LeaderSerializer
from .agenda        import AgendaItemSerializer
from .news          import (
    NewsCategorySerializer,
    NewsListSerializer,
    NewsDetailSerializer,
)
from .event         import EventSerializer
from .gallery       import (
    GalleryCategorySerializer,
    GalleryImageSerializer,
)
from .member        import MemberRegistrationSerializer
from .contact       import ContactMessageSerializer
from .donation      import DonationSerializer
from .testimonial   import TestimonialSerializer
from .subscriber    import SubscriberSerializer
from .site_settings import SiteSettingsSerializer
from .stats         import StatsSerializer

__all__ = [
    # Geography
    'CountySerializer',

    # People
    'LeaderSerializer',

    # Content
    'AgendaItemSerializer',
    'NewsCategorySerializer',
    'NewsListSerializer',
    'NewsDetailSerializer',
    'EventSerializer',
    'GalleryCategorySerializer',
    'GalleryImageSerializer',

    # Forms / submissions
    'MemberRegistrationSerializer',
    'ContactMessageSerializer',
    'DonationSerializer',

    # Engagement
    'TestimonialSerializer',
    'SubscriberSerializer',

    # Config
    'SiteSettingsSerializer',

    # Aggregates
    'StatsSerializer',
]