from django.urls import path
from . import views

urlpatterns = [
    path('charge/', views.charge, name="charge"),
    path('new_donation/', views.new_donation, name="new_donation"),
]