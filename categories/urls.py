from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('deep-dive/<str:category_slug>/', views.deep_dive, name='deep_dive'),
    path('<str:category_slug>/', views.detail, name='detail')
]
