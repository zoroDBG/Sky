from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base),
    path('', views.home),
]