from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Favorite
User = get_user_model()
from projects.models import Project
from rent.models import RentalProperty,VisitSchedule
from rest_framework import generics
from projects.models import Enquiry
from rest_framework.generics import RetrieveAPIView
from home.models import (
        Setting,
        Slider,
        Leadership,
        Why_Choose,
        About, 
        Contact_Page,
        Our_Team,
        Testimonial,
        FAQ,
        ImpactMetric,
        Service,
        FooterLink,
        ContactEnquiry,
    )


from .serializers import (
    ProjectDetailSerializer,
    ProjectSerializer,
    RentalPropertySerializer,
    RegisterSerializer,
    ProfileSerializer,
    RentalDetailSerializer,
    VisitScheduleSerializer,
    SliderSerializer,
    LeadershipSerializer,
    EnquirySerializer,
    WhyChooseSerializer, 
    AboutSerializer, 
    ContactPageSerializer,
    SettingSerializer,
    OurTeamSerializer,
    TestimonialSerializer,
    FAQSerializer,

)


class ProjectListAPIView(generics.ListAPIView):

    queryset = Project.objects.filter(active=True)
    serializer_class = ProjectSerializer


class RentalListAPIView(generics.ListAPIView):

    queryset = RentalProperty.objects.filter(active=True)
    serializer_class = RentalPropertySerializer


class ProjectDetailAPIView(RetrieveAPIView):

    queryset = Project.objects.filter(active=True)

    serializer_class = ProjectDetailSerializer

    lookup_field = "slug"    

class RegisterAPIView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer    

class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)    
    
class RentalDetailAPIView(RetrieveAPIView):

    queryset = RentalProperty.objects.filter(
        active=True
    )

    serializer_class = RentalDetailSerializer

    lookup_field = "slug"

class SearchAPIView(APIView):

    def get(self, request):

        query = request.GET.get("q", "")
        search_type = request.GET.get("type", "all")

        data = {}

        if search_type in ["all", "project"]:

            projects = Project.objects.filter(
                active=True
            ).filter(
                Q(project_name__icontains=query) |
                Q(city__name__icontains=query) |
                Q(locality__name__icontains=query)
            )

            data["projects"] = ProjectSerializer(
                projects,
                many=True
            ).data

        if search_type in ["all", "rent"]:

            rentals = RentalProperty.objects.filter(
                active=True
            ).filter(
                Q(title__icontains=query) |
                Q(city__name__icontains=query) |
                Q(locality__name__icontains=query)
            )

            data["rentals"] = RentalPropertySerializer(
                rentals,
                many=True
            ).data

        return Response(data)

class AddFavoriteAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        project_id = request.data.get("project_id")
        rental_id = request.data.get("rental_id")

        if project_id:

            Favorite.objects.get_or_create(
                user=request.user,
                project_id=project_id
            )

        if rental_id:

            Favorite.objects.get_or_create(
                user=request.user,
                rental_id=rental_id
            )

        return Response({
            "message": "Added to favorites"
        })

class FavoriteListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        favorites = Favorite.objects.filter(
            user=request.user
        )

        serializer = FavoriteSerializer(
            favorites,
            many=True
        )

        return Response(serializer.data)        

class RemoveFavoriteAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        favorite_id = request.data.get("favorite_id")

        Favorite.objects.filter(
            id=favorite_id,
            user=request.user
        ).delete()

        return Response({
            "message": "Removed Successfully"
        })

class EnquiryAPIView(generics.CreateAPIView):

    queryset = Enquiry.objects.all()

    serializer_class = EnquirySerializer

    def perform_create(self, serializer):
        serializer.save()

class VisitScheduleAPIView(generics.CreateAPIView):

    queryset = VisitSchedule.objects.all()

    serializer_class = VisitScheduleSerializer

class SettingAPIView(RetrieveAPIView):

    serializer_class = SettingSerializer

    def get_object(self):
        return Setting.objects.first()    

class SliderListAPIView(generics.ListAPIView):

    queryset = Slider.objects.filter(
        is_active=True
    )

    serializer_class = SliderSerializer

class LeadershipListAPIView(generics.ListAPIView):

    queryset = Leadership.objects.filter(
        is_active=True
    )

    serializer_class = LeadershipSerializer

class WhyChooseListAPIView(generics.ListAPIView):

    queryset = Why_Choose.objects.filter(is_active=True)

    serializer_class = WhyChooseSerializer

class AboutAPIView(generics.RetrieveAPIView):

    serializer_class = AboutSerializer

    def get_object(self):

        return About.objects.filter(is_active=True).first()

class ContactPageAPIView(generics.RetrieveAPIView):

    serializer_class = ContactPageSerializer

    def get_object(self):
        return Contact_Page.objects.first()

class OurTeamListAPIView(generics.ListAPIView):

    queryset = Our_Team.objects.all()

    serializer_class = OurTeamSerializer

class TestimonialListAPIView(generics.ListAPIView):

    queryset = Testimonial.objects.all()

    serializer_class = TestimonialSerializer


class FAQListAPIView(generics.ListAPIView):

    queryset = FAQ.objects.all()

    serializer_class = FAQSerializer
























