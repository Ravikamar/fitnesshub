from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('category/<slug:category_slug>/', views.shop_home, name='product_list_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('order/create/<int:product_id>/', views.order_create, name='order_create'),
]
