from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('register/', views.register),

    path('login/', views.user_login),

    path('booking/', views.booking),

    path('gallery/', views.gallery),

    path('photographer/', views.photographer),

    path('testimonials/', views.testimonials),

    path('logout/', views.user_logout, name='logout'),
]