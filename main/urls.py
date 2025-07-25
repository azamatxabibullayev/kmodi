from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('salfedjio/', views.salfedjio_view, name='salfedjio'),
    path('search/', views.search_view, name='search'),
]
