from django.urls import path

from catalog import views

app_name='catalog'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
