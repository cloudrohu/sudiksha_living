from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import FurnishingItem, Facility


# =========================================================
# 🛋 Furnishing Item Admin
# =========================================================

@admin.register(FurnishingItem)
class FurnishingItemAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'icon_preview',
        'icon',
        'is_active',
    )

    search_fields = ('name',)

    list_filter = ('is_active',)

    def icon_preview(self, obj):

        if obj.icon:
            return mark_safe(
                f'''
                <i class="{obj.icon}"
                   style="
                        font-size:22px;
                        color:#0f172a;
                   ">
                </i>
                '''
            )

        return "-"

    icon_preview.short_description = "Preview"


# =========================================================
# 🏢 Facility Admin
# =========================================================

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'icon_preview',
        'icon',
        'is_active',
    )

    search_fields = ('name',)

    list_filter = ('is_active',)

    def icon_preview(self, obj):

        if obj.icon:
            return mark_safe(
                f'''
                <i class="{obj.icon}"
                   style="
                        font-size:22px;
                        color:#0f172a;
                   ">
                </i>
                '''
            )

        return "-"

    icon_preview.short_description = "Preview"


class FurnishingItemAdmin(admin.ModelAdmin):

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css',
            )
        }