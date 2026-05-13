from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import PropertyAmenities, FurnishingItem, Facility, TenantType

# Placeholder image
NO_IMAGE_URL = "https://via.placeholder.com/40x40.png?text=No+Image"


# =======================================================
# 🔥 Common Safe Preview Function
# =======================================================

def get_image_preview(icon):

    if icon:

        try:
            # ImageField/FileField case
            image_url = icon.url

        except Exception:
            # String path case
            image_url = str(icon)

        return mark_safe(
            f'''
            <img src="{image_url}"
                 width="40"
                 height="40"
                 style="
                    object-fit:contain;
                    border-radius:6px;
                    border:1px solid #ddd;
                    padding:2px;
                    background:#fff;
                 "
            />
            '''
        )

    return mark_safe(
        f'''
        <img src="{NO_IMAGE_URL}"
             width="40"
             height="40"
             style="
                object-fit:contain;
                border-radius:6px;
                border:1px solid #ddd;
                padding:2px;
                background:#fff;
             "
        />
        '''
    )


# =======================================================
# 🏠 Property Amenities Admin
# =======================================================

@admin.register(PropertyAmenities)
class PropertyAmenitiesAdmin(admin.ModelAdmin):

    list_display = ('name', 'icon_preview')
    search_fields = ('name',)
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        return get_image_preview(obj.icon)

    icon_preview.short_description = "Icon"


# =======================================================
# 🛋 Furnishing Item Admin
# =======================================================

@admin.register(FurnishingItem)
class FurnishingItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active', 'icon_preview')
    list_filter = ('is_active',)
    search_fields = ('name',)
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        return get_image_preview(obj.icon)

    icon_preview.short_description = "Icon"


# =======================================================
# 🏢 Facility Admin
# =======================================================

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


# =======================================================
# 👥 Tenant Type Admin
# =======================================================

@admin.register(TenantType)
class TenantTypeAdmin(admin.ModelAdmin):

    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)