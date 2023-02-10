from django.urls import path
from . import views

urlpatterns = [
    path('ex02/init', views.init, name='init'),
    path('ex02/populate', views.populate, name='populate'),
    path('ex02/display', views.display, name='display'),
]