from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shop"),
    path('<slug:slug>/', views.index, name="shop_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_details, name="product"),
]

