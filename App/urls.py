from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('security_alerts/', views.security_alerts, name='security_alerts'),
    path('capture_traffic/', views.capture_traffic, name='capture_traffic'),
]
