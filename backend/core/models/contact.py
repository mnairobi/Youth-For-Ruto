from django.db import models


class ContactMessage(models.Model):

    SUBJECT_CHOICES = [
        ('general',     'General Inquiry'),
        ('membership',  'Membership'),
        ('events',      'Events'),
        ('partnership', 'Partnership'),
        ('media',       'Media Inquiry'),
        ('complaint',   'Complaint / Feedback'),
    ]

    # ── Sender details ────────────────────────────────────────────
    full_name = models.CharField(max_length=200)
    email     = models.EmailField()
    phone     = models.CharField(max_length=15, blank=True)

    # ── Message ───────────────────────────────────────────────────
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()

    # ── Admin controls ────────────────────────────────────────────
    is_read    = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} – {self.get_subject_display()}'