from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the homepage
    path('calculate/', views.calculate_power, name='calculate_power'),  # Route for calculating power
]
