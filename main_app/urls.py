from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('planets/', views.planets_index, name='planets'),
    path('herbs/', views.herbs_index, name='herbs'),
    path('about/', views.about, name='about'),
    path('body_system/', views.bodysystems_index, name='bodysystem'),
    path('<str:herb>/', views.herb, name='herb'),
]