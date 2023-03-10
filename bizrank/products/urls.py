from django.urls import path

from . import views

urlpatterns = [
    path('<int:product_id>/', views.detail, name='detail'),
    path('add/', views.create_product, name='add'),
    path('delete/', views.delete_product, name='delete'),
]