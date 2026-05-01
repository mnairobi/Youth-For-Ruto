from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .county import County


class Event(models.Model):

    STATUS_CHOICES = [
        ('upcoming',  'Upcoming'),
        ('ongoing',   'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    # ── Core fields ────────────────────────────────────────────────
    title = models.CharField(max_length=300)
    slug  = models.SlugField(unique=True, max_length=300)

    # ── Content ───────────────────────────────────────────────────
    description       = RichTextUploadingField()
    short_description = models.TextField(max_length=500)
    image             = models.ImageField(upload_to='events/', blank=True)

    # ── Logistics ─────────────────────────────────────────────────
    venue  = models.CharField(max_length=300)
    county = models.ForeignKey(
        County,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='events',
    )
    date       = models.DateField()
    start_time = models.TimeField()
    end_time   = models.TimeField(null=True, blank=True)

    # ── Admin controls ────────────────────────────────────────────
    status            = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    registration_link = models.URLField(blank=True)
    is_featured       = models.BooleanField(default=False)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-date']

    def __str__(self):
        return self.title