from django.urls import path,include
from . import views

urlpatterns = [
        path('', views.bookings, name='book'),
        path('history', views.history, name='history'),
        path('update_booking/<int:id>', views.update_booking, name='update_booking'),
]