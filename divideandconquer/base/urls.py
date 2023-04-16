from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_client/', views.login_client, name='login_client'),
    path('register_client/', views.register_client, name='register_client'),
    path('client_request/', views.client_requests, name = 'client_requests'),
]