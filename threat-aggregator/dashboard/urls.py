from django.urls import path
from . import views

urlpatterns = [
    path('', views.ioc_list, name='ioc_list'),
]
