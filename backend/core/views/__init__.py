# ---------------------------------------------------------------------------
# core/views/__init__.py
#
# Re-export every view so that urls.py can still do:
#
#   from core.views import CountyViewSet, LeaderViewSet, ...
#   from core.views import site_settings, stats
#
# ---------------------------------------------------------------------------

# ── ViewSets ─────────────────────────────────────────────────────────────
from .county      import CountyViewSet
from .leader      import LeaderViewSet
from .agenda      import AgendaItemViewSet
from .news        import NewsCategoryViewSet, NewsArticleViewSet
from .event       import EventViewSet
from .gallery     import GalleryCategoryViewSet, GalleryImageViewSet
from .testimonial import TestimonialViewSet

# ── Generic create views ──────────────────────────────────────────────────
from .member      import MemberRegistrationView
from .contact     import ContactMessageView
from .donation    import DonationView
from .subscriber  import SubscriberView

# ── Function-based views ──────────────────────────────────────────────────
from .settings    import site_settings
from .stats       import stats


__all__ = [
    # ViewSets
    'CountyViewSet',
    'LeaderViewSet',
    'AgendaItemViewSet',
    'NewsCategoryViewSet',
    'NewsArticleViewSet',
    'EventViewSet',
    'GalleryCategoryViewSet',
    'GalleryImageViewSet',
    'TestimonialViewSet',

    # Generic create views
    'MemberRegistrationView',
    'ContactMessageView',
    'DonationView',
    'SubscriberView',

    # Function-based views
    'site_settings',
    'stats',
]