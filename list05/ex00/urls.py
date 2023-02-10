from django.urls import path
from . import views

urlpatterns = [
    path('ex00/init', views.index, name='index'),
]