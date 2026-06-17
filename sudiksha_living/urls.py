from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.sitemaps.views import sitemap 
from projects.sitemaps import ProjectSitemap 
from properties.sitemaps import PropertySitemap, BlogSitemap, StaticSitemap 

from projects .views import *   

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Define the dictionary of sitemaps
sitemaps = {
    'static': StaticSitemap,
    'properties': PropertySitemap,
    'projects': ProjectSitemap, 
    'blog': BlogSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),   # 👈 YAHIN SE home-contact aayega
    path('', include('utility.urls')),
    path('rent/', include('rent.urls')),
    path('projects/', include('projects.urls')),
    path('properties/', include('properties.urls')),
    path('accounts/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("api/", include("api.urls")),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),

    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)