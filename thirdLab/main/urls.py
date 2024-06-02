from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='mainPage'),
    path('about/', views.about, name='aboutPage')
]
