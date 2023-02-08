from . views import *
from forms import views

from django.urls import path

urlpatterns = [
    path('', views.contact, name="home"),
    path('home/', views.contact, name='contact'),
    path('completed/', views.complete),
]
