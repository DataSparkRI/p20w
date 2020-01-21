from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home_page'),
    path('deep-dive/<str:category_slug>/', views.deepdive_page, name='deepdive_page'),
    path('<str:category_slug>/', views.category_page, name='category_page'),
    path('deep-dive/<str:category_slug>/<str:indicator_id>/', views.deepdive_page_single, name='deepdive_page_single')
]
