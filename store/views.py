from django.http import request
from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.

def categories(request):
    return {'categories': Category.objects.all() }

def product_all(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'product': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})
