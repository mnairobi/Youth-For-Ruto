from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AgendaItem(models.Model):

    ICON_CHOICES = [
        ('briefcase',  'Briefcase / Jobs'),
        ('graduation', 'Graduation / Education'),
        ('chart',      'Chart / Economy'),
        ('shield',     'Shield / Security'),
        ('heart',      'Heart / Health'),
        ('seedling',   'Seedling / Agriculture'),
        ('laptop',     'Laptop / Digital'),
        ('home',       'Home / Housing'),
        ('users',      'Users / Unity'),
        ('globe',      'Globe / Foreign Policy'),
        ('lightbulb',  'Lightbulb / Innovation'),
        ('handshake',  'Handshake / Partnership'),
    ]

    # ── Core fields ────────────────────────────────────────────────
    title = models.CharField(max_length=200)
    slug  = models.SlugField(unique=True)
    icon  = models.CharField(max_length=20, choices=ICON_CHOICES, default='briefcase')

    # ── Content ───────────────────────────────────────────────────
    short_description = models.TextField(max_length=300)
    full_description  = RichTextUploadingField(blank=True)
    image             = models.ImageField(upload_to='agenda/', blank=True)

    # ── Admin controls ────────────────────────────────────────────
    order     = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Agenda Item'
        verbose_name_plural = 'Agenda Items'
        ordering = ['order']

    def __str__(self):
        return self.title