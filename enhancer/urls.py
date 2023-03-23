from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.first, name='enhancer-first'),
    path('home', views.home, name='enhancer-home'),
    path('aboutus/', views.aboutus, name='enhancer-aboutus'),
    path('ai_app/', views.ai_app, name='enhancer-ai_app'),
    path('result/', views.result, name='enhancer-result'),
]