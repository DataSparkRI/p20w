from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:category_id>/', views.detail, name='detail')
]