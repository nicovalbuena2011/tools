
from django.urls import path
from . import views

app_name = 'calculadora'

urlpatterns = [
    path('welcome-experience/', views.welcome, name = 'welcome' ),
    path('validate-experience/', views.validar_experiencia, name = 'validar-experiencia' ),  
]
