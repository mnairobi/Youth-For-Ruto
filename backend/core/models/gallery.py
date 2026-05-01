from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Gallery Category'
        verbose_name_plural = 'Gallery Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class GalleryImage(models.Model):

    # ── Core fields ────────────────────────────────────────────────
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')

    # ── Relations ─────────────────────────────────────────────────
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='images',
    )

    # ── Content ───────────────────────────────────────────────────
    caption = models.TextField(blank=True)

    # ── Admin controls ────────────────────────────────────────────
    is_featured = models.BooleanField(default=False)

    # ── Timestamps ────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
        ordering = ['-created_at']

    def __str__(self):
        return self.title