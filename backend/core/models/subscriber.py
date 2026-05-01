from django.db import models


class Subscriber(models.Model):

    # ── Contact details ───────────────────────────────────────────
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)

    # ── Admin controls ────────────────────────────────────────────
    is_active = models.BooleanField(default=True)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        ordering = ['-created_at']

    def __str__(self):
        return self.email