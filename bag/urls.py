from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/product/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/product/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/product/<item_id>/', views.remove_from_bag, 
        name='remove_from_bag'),
    path('add/series/<item_id>/', views.add_series_to_bag, 
        name='add_series_to_bag'),
    path('adjust/series/<item_id>/', views.adjust_series_in_bag, 
        name='adjust_series_in_bag'),
    path('remove/series/<item_id>/', views.remove_series_from_bag, 
        name='remove_series_from_bag'),
    path('add/token/<item_id>/', views.add_token_to_bag, 
        name='add_token_to_bag'),
    path('adjust/token/<item_id>/', views.adjust_token_in_bag, 
        name='adjust_token_in_bag'),
    path('remove/token/<item_id>/', views.remove_token_from_bag, 
        name='remove_token_from_bag'),
]
