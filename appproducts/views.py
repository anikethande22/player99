from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm
from bookings.models import Bookings
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.
def products(request):
    products = Products.objects.all()
    return render(request,'products/products.html', {"products": products})

def delete_products(request, id):
    products = Products.objects.get(id=id)
    products.delete()
    return redirect('products')

def products_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            p_form = ProductForm()
        else:
            data = Products.objects.get(id=id)
            p_form = ProductForm(instance=data)
        return render(request, 'products/products_form.html',{"p_form": p_form})

    if request.method == "POST":
        if id == 0:
            p_form = ProductForm(request.POST, request.FILES)
        else:
            data = Products.objects.get(id=id)
            p_form = ProductForm(request.POST, request.FILES, instance=data)

        if p_form.is_valid():
            p_form.save()
        
    return redirect('products')


def place_order(request, id):
    user_id = User.objects.get(id=request.user.id)
    product_id = Products.objects.get(id=id)
    bookingdate = datetime.now()
    quantity = 1
    cost = product_id.price * quantity
    isdelivered = False
    order = Bookings(productsid=product_id, userid=user_id, bookingdate=bookingdate, cost=cost, quantity=quantity, isdelivered=isdelivered)
    order.save()
    return redirect('book')


