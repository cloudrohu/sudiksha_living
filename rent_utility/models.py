from django.db import models


# =========================================================
# 🛋 Furnishing Item
# =========================================================

class FurnishingItem(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    icon = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        help_text="Example: fa-solid fa-bed"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Furnishing Item"
        verbose_name_plural = "Furnishing Items"
        ordering = ['name']

    def __str__(self):
        return self.name


# =========================================================
# 🏢 Facility
# =========================================================

class Facility(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Example: fa-solid fa-car"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"
        ordering = ['name']

    def __str__(self):
        return self.name