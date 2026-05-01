from django.db import models


class Testimonial(models.Model):

    # ── Person details ────────────────────────────────────────────
    name     = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    photo    = models.ImageField(upload_to='testimonials/', blank=True)
    role     = models.CharField(max_length=200, blank=True)

    # ── Content ───────────────────────────────────────────────────
    quote = models.TextField()

    # ── Admin controls ────────────────────────────────────────────
    is_active = models.BooleanField(default=True)
    order     = models.PositiveIntegerField(default=0)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['order']

    def __str__(self):
        return f'{self.name} – {self.location}'