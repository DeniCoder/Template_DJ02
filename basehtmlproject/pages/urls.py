from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('services/', views.services, name='services'),  # Страница "Услуги"
    path('contact/', views.contact, name='contact'),  # Страница "Контакты"
]