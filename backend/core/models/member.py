from django.db import models
from .county import County


class MemberRegistration(models.Model):

    GENDER_CHOICES = [
        ('male',   'Male'),
        ('female', 'Female'),
        ('other',  'Other'),
    ]

    # ── Personal details ──────────────────────────────────────────
    full_name   = models.CharField(max_length=200)
    phone       = models.CharField(max_length=15)
    email       = models.EmailField(blank=True)
    gender      = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # ── Location ──────────────────────────────────────────────────
    county     = models.ForeignKey(
        County,
        on_delete=models.SET_NULL,
        null=True,
        related_name='members',
    )
    constituency = models.CharField(max_length=200)
    ward       = models.CharField(max_length=200)

    # ── Admin controls ────────────────────────────────────────────
    is_verified = models.BooleanField(default=False)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name          = 'Member Registration'
        verbose_name_plural   = 'Member Registrations'
        ordering              = ['-created_at']

    def __str__(self):
        return f'{self.full_name} – {self.county}'