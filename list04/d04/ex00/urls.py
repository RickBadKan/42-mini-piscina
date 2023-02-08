from django.urls import path

from . import views

urlpatterns = [
    path('ex00/', views.index, name='index'),
]