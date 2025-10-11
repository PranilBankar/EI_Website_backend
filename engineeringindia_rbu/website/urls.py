from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('api/members/', views.get_members, name='get_members'),
    path('api/projects/', views.get_projects, name='get_projects'),
    path('api/events/', views.get_events, name='get_events'),
]
