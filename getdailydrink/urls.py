from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('create/', views.log_water, name='log_water'),
]