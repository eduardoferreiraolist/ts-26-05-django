from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list', views.product_list),
    path('form', views.product_form),
    path('categories/list', views.categories_list),
    path('categories/form', views.categories_form),
]
