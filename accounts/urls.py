from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from . import views

urlpatterns = [
path('', views.dashboard , name='dashboard'),
# path('', TemplateView.as_view(template_name='home.html')),
]