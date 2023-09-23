from django.urls import path
from . import views

urlpatterns = [
    path('create_food_item/', views.create_food_item, name='create_food_item'),
    path('create_donor/', views.create_donor, name='create_donor'),
    # Add more URL patterns as needed
]