from django.urls import path,include
from . import views

urlpatterns = [
        path('', views.products, name='products'),
        path('delete_products/<int:id>', views.delete_products, name='delete_products'),
        path('add_products', views.products_form, name='add_products'),
        path('update_products/<int:id>', views.products_form, name='update_products'),
        path('place_order/<int:id>', views.place_order, name='place_order'),
]