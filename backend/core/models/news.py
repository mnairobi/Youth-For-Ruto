from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class NewsArticle(models.Model):

    # ── Core fields ────────────────────────────────────────────────
    title = models.CharField(max_length=300)
    slug  = models.SlugField(unique=True, max_length=300)

    # ── Relations ─────────────────────────────────────────────────
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles',
    )

    # ── Content ───────────────────────────────────────────────────
    excerpt        = models.TextField(max_length=500)
    content        = RichTextUploadingField()
    featured_image = models.ImageField(upload_to='news/')
    author         = models.CharField(max_length=200, default='YR27 Media Team')

    # ── Admin controls ────────────────────────────────────────────
    is_featured  = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    views        = models.PositiveIntegerField(default=0)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'News Article'
        verbose_name_plural = 'News Articles'
        ordering = ['-created_at']

    def __str__(self):
        return self.title