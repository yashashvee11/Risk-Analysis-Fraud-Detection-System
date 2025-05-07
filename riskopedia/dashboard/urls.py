from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path('dashboard/', views.dashboardView, name='dashboardView'),
]
