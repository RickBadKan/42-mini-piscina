from django.urls import path

from . import views

urlpatterns = [
    path('ex01/django/', views.django_page),
    path('ex01/display/', views.display_page),
    path('ex01/templates/', views.templates_page),
]