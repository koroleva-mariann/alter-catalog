from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/list', views.product_list, name='product_list'),
    path('product/update', views.product_update, name='product_update'),
    path('product/pricelog', views.pricelog_list, name='product_pricelog'),
]
