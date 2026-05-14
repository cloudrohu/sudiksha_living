from django.contrib import admin
from django.utils.html import mark_safe

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
                     width="100"
                     height="70"
                     style="
                        object-fit:cover;
                        border-radius:8px;
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
# 🏠 PROPERTY INLINE INSIDE OWNER
# =========================================================

class RentalPropertyInline(admin.TabularInline):

    model = RentalProperty

    extra = 0

    show_change_link = True

    fields = (
        'title',
        'city',
        'locality',
        'project',
        'bedrooms',
        'bathrooms',
        'super_area',
        'active',
    )


# =========================================================
# 👤 OWNER PROFILE ADMIN
# =========================================================

@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'phone',
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

    inlines = [
        RentalPropertyInline
    ]


# =========================================================
# 🏠 RENTAL PROPERTY ADMIN
# =========================================================

@admin.register(RentalProperty)
class RentalPropertyAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'owner',
        'city',
        'locality',
        'project',
        'bedrooms',
        'bathrooms',
        'super_area',
        'featured_property',
        'active',
        'created_at',
    )

    search_fields = (
        'title',
        'owner__full_name',
        'city__name',
        'locality__name',
    )

    list_filter = (
        'city',
        'featured_property',
        'active',
        'furnishing_type',
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

        # 🖼 Property Images
        RentalPropertyImageInline,

        # 📝 About
        AboutPropertyInline,

        # 📍 Connectivity
        RentalConnectivityInline,

        # 🏡 Amenities
        RentalAmenityInline,

        # 🛋 Furnishing
        FurnishingAmenityInline,

        # 🏢 Facilities
        RentalFacilityInline,

        # 💰 Charges
        ChargesDetailsInline,

        # ❓ FAQ
        RentalFAQInline,
    ]


# =========================================================
# 📩 RENTAL ENQUIRY ADMIN
# =========================================================

@admin.register(RentalEnquiry)
class RentalEnquiryAdmin(admin.ModelAdmin):

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