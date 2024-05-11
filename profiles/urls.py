from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('library/', views.library, name='library'),
    path('series_library/<int:series_no>/', views.series_library, name='series_library'),
    path('product_viewer/<int:product_id>/', views.product_viewer, name='product_viewer'),
]
