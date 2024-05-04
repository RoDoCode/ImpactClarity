from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('add/<item_id>/', views.add_series_to_bag, name='add_series_to_bag'),
    path('adjust/<item_id>/', views.adjust_series_in_bag, name='adjust_series_in_bag'),
    path('remove/<item_id>/', views.remove_series_from_bag, name='remove_series_from_bag'),
    path('add/<item_id>/', views.add_token_to_bag, name='add_token_to_bag'),
    path('adjust/<item_id>/', views.adjust_token_in_bag, name='adjust_token_in_bag'),
    path('remove/<item_id>/', views.remove_token_from_bag, name='remove_token_from_bag'),
]
