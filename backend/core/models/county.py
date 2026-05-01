from django.db import models


class County(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    registered_youth = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'County'
        verbose_name_plural = 'Counties'
        ordering = ['name']

    def __str__(self):
        return self.name