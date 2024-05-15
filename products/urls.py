from django.urls import path
from . import views
from .views import series_detail


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/product', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
    path('series/<int:series_no>/', series_detail, name='series_detail'),
    path('series/all/', views.series, name='series'),
    path('add/series', views.add_series, name='add_series'),
    path('edit/<int:series_id>/', views.edit_series, name='edit_series'),
    path('delete/<int:series_id>/',
         views.delete_series,
         name='delete_series'),
]
