from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ImportExportModelAdmin

from .models import (
    OwnerProfile,
    RentalProperty,
    RentalPropertyImage,
    AboutProperty,
    RentalConnectivity,
    RentalAmenity,
    FurnishingAmenity,
    RentalFacility,
    ChargesDetails,
    RentalFAQ,
    RentalEnquiry,
)


# =========================================================
# 🖼 PROPERTY IMAGE INLINE
# =========================================================

class RentalPropertyImageInline(admin.TabularInline):

    model = RentalPropertyImage
    extra = 1

    fields = (
        'image',
        'image_preview',
        'alt_text',
        'is_primary',
    )

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):

        if obj.image:
            return mark_safe(
                f'''
                <img src="{obj.image.url}"
                     width="120"
                     height="80"
                     style="
                        object-fit:cover;
                        border-radius:10px;
                        border:1px solid #ddd;
                     "
                />
                '''
            )

        return "No Image"

    image_preview.short_description = "Preview"


# =========================================================
# 📝 ABOUT PROPERTY INLINE
# =========================================================

class AboutPropertyInline(admin.StackedInline):

    model = AboutProperty
    extra = 0


# =========================================================
# 📍 CONNECTIVITY INLINE
# =========================================================

class RentalConnectivityInline(admin.TabularInline):

    model = RentalConnectivity
    extra = 1


# =========================================================
# 🏡 AMENITY INLINE
# =========================================================

class RentalAmenityInline(admin.TabularInline):

    model = RentalAmenity
    extra = 1

    autocomplete_fields = ['amenity']


# =========================================================
# 🛋 FURNISHING INLINE
# =========================================================

class FurnishingAmenityInline(admin.TabularInline):

    model = FurnishingAmenity
    extra = 1

    autocomplete_fields = ['item']


# =========================================================
# 🏢 FACILITY INLINE
# =========================================================

class RentalFacilityInline(admin.TabularInline):

    model = RentalFacility
    extra = 1

    autocomplete_fields = ['facility']


# =========================================================
# 💰 CHARGES INLINE
# =========================================================

class ChargesDetailsInline(admin.StackedInline):

    model = ChargesDetails
    extra = 0


# =========================================================
# ❓ FAQ INLINE
# =========================================================

class RentalFAQInline(admin.TabularInline):

    model = RentalFAQ
    extra = 1


# =========================================================
# 👤 OWNER PROFILE ADMIN
# =========================================================

@admin.register(OwnerProfile)
class OwnerProfileAdmin(ImportExportModelAdmin):

    list_display = (
        'full_name',
        'phone',
        'email',
        'owner_type',
        'is_verified',
        'is_active',
        'profile_preview',
    )

    search_fields = (
        'full_name',
        'phone',
        'email',
    )

    list_filter = (
        'owner_type',
        'is_verified',
        'is_active',
    )

    readonly_fields = (
        'profile_preview',
        'created_at',
    )

    autocomplete_fields = ['user']

    fieldsets = (

        ('Basic Information', {
            'fields': (
                'user',
                'owner_type',
                'full_name',
                'phone',
                'email',
                'locality',
            )
        }),

        ('Profile', {
            'fields': (
                'profile_image',
                'profile_preview',
                'about',
            )
        }),

        ('Status', {
            'fields': (
                'is_online',
                'is_verified',
                'is_active',
            )
        }),

        ('System', {
            'classes': ('collapse',),
            'fields': (
                'created_at',
            )
        }),
    )


# =========================================================
# 🏠 RENTAL PROPERTY ADMIN
# =========================================================

@admin.register(RentalProperty)
class RentalPropertyAdmin(ImportExportModelAdmin):

    list_display = (
        'property_image',
        'title',
        'city',
        'locality',
        'bedrooms',
        'bathrooms',
        'super_area',
        'furnishing_type',
        'rent_price',
        'featured_property',
        'active',
        'created_at',
    )

    search_fields = (
        'title',
        'city__name',
        'locality__name',
        'owner__full_name',
    )

    list_filter = (
        'city',
        'featured_property',
        'active',
        'furnishing_type',
        'posted_by',
        'available_from',
    )

    ordering = ('-created_at',)

    readonly_fields = (
        'slug',
        'created_at',
        'updated_at',
    )

    autocomplete_fields = (
        'owner',
        'city',
        'locality',
        'project',
    )

    list_editable = (
        'featured_property',
        'active',
    )

    fieldsets = (

        ('Basic Information', {
            'fields': (
                'owner',
                'title',
                'project',
                'city',
                'locality',
                'address',
            )
        }),

        ('Property Details', {
            'fields': (
                'bedrooms',
                'bathrooms',
                'super_area',
                'floor',
                'total_floor',
                'furnishing_type',
                'posted_by',
                'available_from',
                'age_of_property',
            )
        }),

        ('Media & Location', {
            'classes': ('collapse',),
            'fields': (
                'youtube_embed_id',
                'google_map_iframe',
            )
        }),

        ('Status', {
            'fields': (
                'featured_property',
                'active',
                'slug',
            )
        }),

        ('System Information', {
            'classes': ('collapse',),
            'fields': (
                'created_at',
                'updated_at',
                'created_by',
                'updated_by',
            )
        }),
    )

    inlines = [
        RentalPropertyImageInline,
        AboutPropertyInline,
        RentalConnectivityInline,
        RentalAmenityInline,
        FurnishingAmenityInline,
        RentalFacilityInline,
        ChargesDetailsInline,
        RentalFAQInline,
    ]

    # =====================================================
    # IMAGE PREVIEW
    # =====================================================

    def property_image(self, obj):

        image = obj.property_images.first()

        if image and image.image:
            return mark_safe(
                f'''
                <img src="{image.image.url}"
                     width="80"
                     height="60"
                     style="
                        object-fit:cover;
                        border-radius:8px;
                        border:1px solid #ddd;
                     "
                />
                '''
            )

        return "No Image"

    property_image.short_description = "Image"

    # =====================================================
    # RENT PRICE
    # =====================================================

    def rent_price(self, obj):

        if hasattr(obj, 'rent_details'):
            return f"₹ {obj.rent_details.monthly_rent}"

        return "₹ 0"

    rent_price.short_description = "Monthly Rent"

    # =====================================================
    # QUERY OPTIMIZATION
    # =====================================================

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        return qs.select_related(
            'city',
            'locality',
            'owner',
            'project',
        ).prefetch_related(
            'property_images',
        )


# =========================================================
# 📩 RENTAL ENQUIRY ADMIN
# =========================================================

@admin.register(RentalEnquiry)
class RentalEnquiryAdmin(ImportExportModelAdmin):

    list_display = (
        'name',
        'phone',
        'email',
        'rental',
        'created_at',
    )

    search_fields = (
        'name',
        'phone',
        'email',
    )

    list_filter = (
        'created_at',
    )

    ordering = ('-created_at',)