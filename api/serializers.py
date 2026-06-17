from rest_framework import serializers
from rent.models import RentalProperty
from .models import Favorite
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
        ContactEnquiry

    )



from projects.models import (
    Gallery,
    Configuration,
    Amenities,
    ProjectFAQ,
    Connectivity,
    Project,
    Enquiry,
)

from rent.models import (
    RentalProperty,
    RentalPropertyImage,
    ChargesDetails,
    VisitSchedule,
)

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
            "user_type",
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            user_type=validated_data.get(
                "user_type",
                "buyer"
            )
        )

        return user

class ProjectSerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    locality = serializers.StringRelatedField()
    developer = serializers.StringRelatedField()

    class Meta:
        model = Project

        fields = [
            "id",
            "project_name",
            "slug",
            "city",
            "locality",
            "developer",
            "construction_status",
            "featured_property",
            "image",
            "banner_img",
            "google_map_iframe",
        ]


class RentalPropertySerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    locality = serializers.StringRelatedField()

    class Meta:
        model = RentalProperty

        fields = [
            "id",
            "title",
            "slug",
            "bedrooms",
            "bathrooms",
            "super_area",
            "furnishing_type",
            "city",
            "locality",
            "featured_property",
            "created_at",
        ]

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ["id", "image"]

class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuration

        fields = [
            "id",
            "bhk_type",
            "area_sqft",
            "price_in_rupees"
        ]

class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectFAQ

        fields = [
            "question",
            "answer"
        ]

class ProjectDetailSerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    locality = serializers.StringRelatedField()
    developer = serializers.StringRelatedField()

    gallery = GallerySerializer(
        many=True,
        read_only=True
    )

    configurations = ConfigurationSerializer(
        many=True,
        read_only=True
    )

    faqs = FAQSerializer(
        many=True,
        read_only=True
    )

    class Meta:

        model = Project

        fields = [
            "id",
            "project_name",
            "slug",
            "city",
            "locality",
            "developer",
            "construction_status",
            "image",
            "banner_img",
            "gallery",
            "configurations",
            "faqs",
        ]                                

class AmenitySerializer(serializers.ModelSerializer):

    amenity_name = serializers.CharField(
        source="amenities.title",
        read_only=True
    )

    class Meta:
        model = Amenities
        fields = [
            "id",
            "amenity_name"
        ]

class ConnectivitySerializer(serializers.ModelSerializer):


    class Meta:
        model = Connectivity

        fields = [
            "id",
            "title"
        ] 

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "user_type",
            "first_name",
            "last_name",
        ]

class ProjectDetailSerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    locality = serializers.StringRelatedField()
    developer = serializers.StringRelatedField()

    gallery = GallerySerializer(many=True, read_only=True)

    configurations = ConfigurationSerializer(
        many=True,
        read_only=True
    )

    faqs = FAQSerializer(
        many=True,
        read_only=True
    )

    amenities = AmenitySerializer(
        source="project_amenities",
        many=True,
        read_only=True
    )

    connectivity = ConnectivitySerializer(
        many=True,
        read_only=True
    )

    price_range = serializers.SerializerMethodField()

    carpet_area_range = serializers.SerializerMethodField()

    def get_price_range(self, obj):
        return obj.get_price_range()

    def get_carpet_area_range(self, obj):
        return obj.get_carpet_area_range()

    class Meta:

        model = Project

        fields = [
            "id",
            "project_name",
            "slug",
            "city",
            "locality",
            "developer",
            "construction_status",

            "price_range",
            "carpet_area_range",

            "image",
            "banner_img",

            "gallery",
            "configurations",

            "amenities",
            "connectivity",

            "faqs",
        ]

class RentalImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentalPropertyImage

        fields = [
            "id",
            "image",
            "is_primary",
        ]

class ChargesDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargesDetails

        fields = [
            "monthly_rent",
            "security_deposit",
            "paper_charges",
            "moving_charges",
            "preferred_tenant",
            "lease_duration",
        ]

class ChargesDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargesDetails

        fields = [
            "monthly_rent",
            "security_deposit",
            "paper_charges",
            "moving_charges",
            "preferred_tenant",
            "lease_duration",
        ]
        
class RentalDetailSerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    locality = serializers.StringRelatedField()

    class Meta:
        model = RentalProperty

        fields = [
            "id",
            "title",
            "slug",
            "bedrooms",
            "bathrooms",
            "super_area",
            "furnishing_type",
            "address",
            "city",
            "locality",
        ]

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite

        fields = "__all__"       

class EnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Enquiry

        fields = [
            "project",
            "name",
            "email",
            "phone",
            "message",
        ]

class VisitScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitSchedule

        fields = [
            "rental",
            "name",
            "phone",
            "visit_date",
            "visit_time",
        ]

class SettingSerializer(serializers.ModelSerializer):

    logo = serializers.SerializerMethodField()
    favicon = serializers.SerializerMethodField()
    search_bg = serializers.SerializerMethodField()
    testmonial_bg = serializers.SerializerMethodField()

    class Meta:
        model = Setting

        fields = [
            "site_name",

            "logo",
            "favicon",
            "search_bg",
            "testmonial_bg",

            "header_footer_color",
            "text_color",
            "button_color",

            "rera_color",
            "rera_number",

            "address",
            "phone",
            "whatsapp",
            "email",

            "google_map",

            "facebook",
            "instagram",
            "twitter",
            "youtube",

            "footer_text",
            "copy_right",

            "meta_title",
            "meta_description",
            "meta_keywords",
        ]

    def get_logo(self, obj):
        request = self.context.get("request")
        if obj.logo:
            return request.build_absolute_uri(obj.logo.url)
        return None

    def get_favicon(self, obj):
        request = self.context.get("request")
        if obj.favicon:
            return request.build_absolute_uri(obj.favicon.url)
        return None

    def get_search_bg(self, obj):
        request = self.context.get("request")
        if obj.search_bg:
            return request.build_absolute_uri(obj.search_bg.url)
        return None

    def get_testmonial_bg(self, obj):
        request = self.context.get("request")
        if obj.testmonial_bg:
            return request.build_absolute_uri(obj.testmonial_bg.url)
        return None        
    
class SliderSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = Slider

        fields = [
            "id",
            "title",
            "subtitle",
            "image",
            "button_text",
            "button_link",
            "order",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None


class LeadershipSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = Leadership

        fields = [
            "id",
            "name",
            "designation",
            "image",
            "bio",
            "linkedin_url",
            "email",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None


class WhyChooseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Why_Choose

        fields = [
            "id",
            "title",
            "subtitle",
            "order",
        ]


class AboutSerializer(
    serializers.ModelSerializer
):

    search_bg = serializers.SerializerMethodField()
    home_bg = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = About

        fields = "__all__"

    def get_search_bg(self, obj):

        request = self.context.get("request")

        if obj.search_bg:
            return request.build_absolute_uri(
                obj.search_bg.url
            )

        return None

    def get_home_bg(self, obj):

        request = self.context.get("request")

        if obj.home_bg:
            return request.build_absolute_uri(
                obj.home_bg.url
            )

        return None

    def get_image(self, obj):

        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None

class ContactPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact_Page

        fields = [
            "id",
            "heading",
            "sub_heading",
            "address",
            "phone",
            "email",
            "map_iframe",
        ]

class OurTeamSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = Our_Team

        fields = [
            "id",
            "name",
            "designation",
            "image",
            "bio",
        ]

    def get_image(self, obj):

        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None


class TestimonialSerializer(
    serializers.ModelSerializer
):

    image = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial

        fields = [
            "id",
            "name",
            "designation",
            "message",
            "rating",
            "image",
        ]

    def get_image(self, obj):

        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None
    
class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ

        fields = [
            "id",
            "question",
            "answer",
        ]



