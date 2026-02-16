from django.urls import path
from . import views

urlpatterns = [
   path('', views.rent_list, name='rent_list'),
   path('<slug:slug>-rental-details/', views.rental_detail, name='rental_detail'),
   
]