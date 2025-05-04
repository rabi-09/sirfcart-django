from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shop"),
    path('category/<slug:slug>/', views.index, name="shop_by_category"),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_details, name="product"),
]

