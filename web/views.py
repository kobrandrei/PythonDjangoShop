from django.shortcuts import render
from web.models import Product

def index(request):
    return render(request, 'web/index.html')

def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'web/shop.html', context)
