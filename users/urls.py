from django.urls import path,include
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('aboutus', views.aboutus, name='aboutus'),
]