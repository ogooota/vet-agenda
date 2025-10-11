from django.urls import path
from django.template import loader
from . import views

urlpatterns = [
    path('agenda/', views.agenda, name='agenda'),
    path('register/', views.register, name='register'),
    path('show_animals/', views.show_animals, name='show_animals'),
    path('main/', views.main, name='main'), 
]