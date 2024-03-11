from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('planets/', views.planets_index, name='planets'),
    path('herbs/', views.herbs_index, name='herbs'),
]