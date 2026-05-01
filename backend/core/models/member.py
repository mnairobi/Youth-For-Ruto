from django.db import models
from .county import County


class MemberRegistration(models.Model):

    ROLE_CHOICES = [
        ('member',        'Regular Member'),
        ('mobilizer',     'Ward Mobilizer'),
        ('campus_leader', 'Campus Leader'),
        ('coordinator',   'Coordinator'),
        ('volunteer',     'Volunteer'),
    ]

    GENDER_CHOICES = [
        ('male',   'Male'),
        ('female', 'Female'),
        ('other',  'Other'),
    ]

    AGE_CHOICES = [ ]

    # ── Personal details ──────────────────────────────────────────
    full_name   = models.CharField(max_length=200)
    # id_number   = models.CharField(max_length=20, unique=True)
    phone       = models.CharField(max_length=15)
    email       = models.EmailField(blank=True)
    gender      = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age_bracket = models.CharField(max_length=10, choices=AGE_CHOICES)

    # ── Location ──────────────────────────────────────────────────
    county          = models.ForeignKey(
        County,
        on_delete=models.SET_NULL,
        null=True,
        related_name='members',
    )
    sub_county      = models.CharField(max_length=200)
    ward            = models.CharField(max_length=200)
    # polling_station = models.CharField(max_length=200, blank=True)

    # # ── Background ────────────────────────────────────────────────
    # institution   = models.CharField(
    #     max_length=200,
    #     blank=True,
    #     help_text='University / College name if the member is a student.',
    # )
    # occupation    = models.CharField(max_length=200, blank=True)

    # # ── Movement role ─────────────────────────────────────────────
    # role_interest = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    # skills        = models.TextField(blank=True)
    # motivation    = models.TextField(
    #     blank=True,
    #     help_text='Why does this person want to join YR27?',
    # )

    # ── Admin controls ────────────────────────────────────────────
    is_verified = models.BooleanField(default=False)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Member Registration'
        verbose_name_plural = 'Member Registrations'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} – {self.county}'