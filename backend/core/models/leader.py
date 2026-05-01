from django.db import models
from .county import County


class Leader(models.Model):

    LEVEL_CHOICES = [
        ('national',    'National Level'),
        ('county',      'County Level'),
        ('grassroots',  'Grassroots Level'),
    ]

    POSITION_CHOICES = [
        ('convener',            'National Convener'),
        ('deputy_convener',     'Deputy Convener'),
        ('chairperson',         'Chairperson'),
        ('deputy_chairperson',  'Deputy Chairperson'),
        ('secretary_general',   'Secretary General'),
        ('treasurer',           'National Treasurer'),
        ('coordinator',         'National Coordinator'),
        ('county_coordinator',  'County Coordinator'),
        ('sub_county_leader',   'Sub-County Leader'),
        ('campus_leader',       'Campus Leader'),
        ('ward_mobilizer',      'Ward Mobilizer'),
        ('community_organizer', 'Community Organizer'),
        ('other',               'Other'),
    ]

    # ── Core fields ────────────────────────────────────────────────
    full_name    = models.CharField(max_length=200)
    position     = models.CharField(max_length=30, choices=POSITION_CHOICES)
    custom_title = models.CharField(
        max_length=200,
        blank=True,
        help_text='Override the position display name shown on the site.',
    )
    level  = models.CharField(max_length=15, choices=LEVEL_CHOICES, default='national')
    county = models.ForeignKey(
        County,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leaders',
    )

    # ── Profile ────────────────────────────────────────────────────
    photo = models.ImageField(upload_to='leaders/', blank=True)
    bio   = models.TextField(blank=True)

    # ── Contact ───────────────────────────────────────────────────
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    # ── Social media ──────────────────────────────────────────────
    twitter   = models.URLField(blank=True)
    facebook  = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    tiktok    = models.URLField(blank=True)

    # ── Admin controls ────────────────────────────────────────────
    order     = models.PositiveIntegerField(default=0, help_text='Lower number = appears first.')
    is_active = models.BooleanField(default=True)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Leader'
        verbose_name_plural = 'Leaders'
        ordering = ['order', 'full_name']

    # ── Helpers ───────────────────────────────────────────────────
    def __str__(self):
        return f'{self.full_name} – {self.display_title}'

    @property
    def display_title(self) -> str:
        """Return custom_title when set, otherwise fall back to the position label."""
        return self.custom_title or self.get_position_display()