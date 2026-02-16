from django.shortcuts import render
from home.models import Setting
from .models import RentalProperty
from django.shortcuts import get_object_or_404

def rent_list(request):
    settings_obj = Setting.objects.first()
    properties = RentalProperty.objects.filter(active=True)

    return render(request, 'rent/rent_list.html', {
        "settings_obj": settings_obj,
        "properties": properties,
    })


def rental_detail(request, slug):
    settings_obj = Setting.objects.first()

    property_obj = get_object_or_404(
        RentalProperty.objects.select_related(
            "city", "locality", "project", "tenant_type", "furnishing_type"
        ).prefetch_related(
            "connectivities",
            "amenities",
            "furnishings",
            "facilities",
            "owner_details",
            "faqs",
        ),
        slug=slug,
        active=True
    )

    return render(request, 'rent/rental_detail.html', {
        "settings_obj": settings_obj,
        "property": property_obj,
    })


def thank_you(request):
    return render(request, "projects/thank_you.html")