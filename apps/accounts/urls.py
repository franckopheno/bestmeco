# apps/accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/boutique/', views.register_boutique, name='register_boutique'),
]