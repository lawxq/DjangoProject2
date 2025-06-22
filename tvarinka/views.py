from django.shortcuts import render
from .models import ClothingItem

def home(request):
    return render(request, 'home.html', {'title': 'Магазин одягу'})

def about(request):
    return render(request, 'about.html', {'title': 'Про нас'})

def clothes(request):
    items = ClothingItem.objects.filter(available=True)
    return render(request, 'clothes.html', {'title': 'Одяг', 'items': items})

def contacts(request):
    return render(request, 'contacts.html', {'title': 'Контакти'})