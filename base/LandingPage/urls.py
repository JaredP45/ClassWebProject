from django.urls import path
from . import views

urlpatterns = [
    path('', views.upper, name='home'),
]
