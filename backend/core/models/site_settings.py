from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class SiteSettings(models.Model):
    """
    Singleton model — only one row is ever created (pk=1).
    Use SiteSettings.load() everywhere instead of .objects.get(pk=1).
    """

    # ── Identity ──────────────────────────────────────────────────
    site_name = models.CharField(max_length=200, default='YR27 – Youths for Ruto 2027')
    tagline   = models.CharField(
        max_length=500,
        default='Youth Power. National Power. 2027 – Ruto Tena.',
    )

    # ── Content ───────────────────────────────────────────────────
    about_text = RichTextUploadingField(blank=True)
    mission    = models.TextField(blank=True)
    vision     = models.TextField(blank=True)

    # ── Contact ───────────────────────────────────────────────────
    phone   = models.CharField(max_length=20, default='+254 XXX XXX XXX')
    email   = models.EmailField(default='info@yr27movement.co.ke')
    address = models.TextField(default='Nairobi, Kenya')

    # ── Social media ──────────────────────────────────────────────
    twitter   = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    tiktok    = models.URLField(blank=True)
    facebook  = models.URLField(blank=True)
    youtube   = models.URLField(blank=True)
    whatsapp  = models.CharField(max_length=20, blank=True)

    # ── Payments ──────────────────────────────────────────────────
    mpesa_paybill = models.CharField(max_length=20, blank=True)
    mpesa_account = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

    # ── Singleton enforcement ─────────────────────────────────────

    def save(self, *args, **kwargs):
        """Always save with pk=1 so only one row ever exists."""
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls) -> 'SiteSettings':
        """Return the single settings row, creating it if needed."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj