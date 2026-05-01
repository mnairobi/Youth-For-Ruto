from django.db import models


class Donation(models.Model):

    PAYMENT_CHOICES = [
        ('mpesa', 'M-Pesa'),
        ('bank',  'Bank Transfer'),
    ]

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('completed', 'Completed'),
        ('failed',    'Failed'),
    ]

    # ── Donor details ─────────────────────────────────────────────
    donor_name = models.CharField(max_length=200)
    phone      = models.CharField(max_length=15)
    email      = models.EmailField(blank=True)

    # ── Transaction details ───────────────────────────────────────
    amount         = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='mpesa')
    transaction_id = models.CharField(max_length=100, blank=True)
    status         = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # ── Optional ──────────────────────────────────────────────────
    message      = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.donor_name} – KES {self.amount}'