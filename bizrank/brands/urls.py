from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:brand_id>/', views.detail, name='detail'),
    path('brand_add/', views.create_brand, name='brand_add'),
    path('brands_delete/', views.delete_brand, name='brands_delete'),
    # path('brands_update/', views.update_brand, name='brands_update'),
    # path('brands_search/', views.search_brand, name='brands_search'),
    path('<int:brand_id>/rate/', views.rate_brand, name='rate'),
    # path('<int:brand_id>/rate/', views.vote, name='rate'),

]