from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'),
   path('contact/', views.Contact.as_view(), name='contact'),
   path('services/', views.Services.as_view(), name='services'),
   path('gallery/', views.Gallery.as_view(), name='gallery'),
   path('about/', views.About.as_view(), name='about'),
]