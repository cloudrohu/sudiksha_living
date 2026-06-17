from django.urls import path

from .views import (
    FavoriteListAPIView,
    AddFavoriteAPIView,
    ProjectDetailAPIView,
    ProjectListAPIView,
    RemoveFavoriteAPIView,
    RentalListAPIView,
    RegisterAPIView,
    ProfileAPIView,
    RentalDetailAPIView,
    SearchAPIView,
    EnquiryAPIView,
    VisitScheduleAPIView,
    SettingAPIView,
    SliderListAPIView,
    LeadershipListAPIView,
    WhyChooseListAPIView,   
    AboutAPIView,
    ContactPageAPIView,
    OurTeamListAPIView,
    TestimonialListAPIView,
    FAQListAPIView

)

urlpatterns = [

    path("projects/",ProjectListAPIView.as_view(),name="api-projects"),

    path("rentals/",RentalListAPIView.as_view(),name="api-rentals"),

    path("project/<slug:slug>/",ProjectDetailAPIView.as_view(),name="api-project-detail"),

    path("register/",RegisterAPIView.as_view(),name="register"),

    path("profile/",ProfileAPIView.as_view(),name="profile"),

    path("rental/<slug:slug>/",RentalDetailAPIView.as_view(),name="api-rental-detail"),
 
    path("search/",SearchAPIView.as_view(),name="api-search"),

    path("favorites/add/",AddFavoriteAPIView.as_view(),name="favorite-add"),

    path("favorites/",FavoriteListAPIView.as_view(),name="favorite-list"),

    path("favorites/remove/",RemoveFavoriteAPIView.as_view(),name="favorite-remove"),

    path("enquiry/",EnquiryAPIView.as_view(),name="enquiry"),

    path("schedule-visit/",VisitScheduleAPIView.as_view(),name="schedule-visit"),

    path("settings/",SettingAPIView.as_view(),name="settings"),

    path("sliders/",SliderListAPIView.as_view(),name="api-sliders"),

    path("leadership/",LeadershipListAPIView.as_view(),name="api-leadership"),

    path("why-choose/",WhyChooseListAPIView.as_view(),name="api-why-choose"),

    path("about/",AboutAPIView.as_view(),name="api-about"),

    path("contact-page/",ContactPageAPIView.as_view(),name="api-contact-page"),

    path("our-team/",OurTeamListAPIView.as_view(),name="api-our-team"),

    path("testimonials/",TestimonialListAPIView.as_view(),name="api-testimonials"),

    path("faqs/",FAQListAPIView.as_view(),name="api-faqs"),
    
]