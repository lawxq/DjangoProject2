from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clothes/', views.clothes, name='clothes'),
    path('contacts/', views.contacts, name='contacts'),
]