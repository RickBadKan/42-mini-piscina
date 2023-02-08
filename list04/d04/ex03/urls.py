from django.urls import path

from . import views

urlpatterns = [
    path('ex03/', views.index, name='index'),
]