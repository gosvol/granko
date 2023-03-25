from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def catalog_of_monuments(request):
    return render(request, 'main/catalog.html')

def types_of_granite(request):
    return render(request, 'main/types.html')

def wholesale_price(request):
    return render(request, 'main/price.html')

def construction(request):
    return render(request, 'main/construction.html')

def album(request):
    return render(request, 'main/album.html')


