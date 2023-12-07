from django.urls import path
from . import views
from .views import *

urlpatterns = [
    
    path('', views.index,name='index'),
    path('api/hotels',api_hotels)
    
]