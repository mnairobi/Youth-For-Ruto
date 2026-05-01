# ---------------------------------------------------------------------------
# core/models/__init__.py
#
# Re-export every model so that the rest of the project can still do:
#
#   from core.models import County, Leader, ...
#
# Django's app-registry and migration engine discover models through this
# file, so every class that needs a DB table must be imported here.
# ---------------------------------------------------------------------------

from .county       import County
from .leader       import Leader
from .agenda       import AgendaItem
from .news         import NewsCategory, NewsArticle
from .event        import Event
from .gallery      import GalleryCategory, GalleryImage
from .member       import MemberRegistration
from .contact      import ContactMessage
from .donation     import Donation
from .testimonial  import Testimonial
from .subscriber   import Subscriber
from .site_settings import SiteSettings

__all__ = [
    # Geography
    'County',

    # People
    'Leader',

    # Content
    'AgendaItem',
    'NewsCategory',
    'NewsArticle',
    'Event',
    'GalleryCategory',
    'GalleryImage',

    # Forms / submissions
    'MemberRegistration',
    'ContactMessage',
    'Donation',

    # Engagement
    'Testimonial',
    'Subscriber',

    # Config
    'SiteSettings',
]