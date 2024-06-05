# views.py

from django.shortcuts import render
from .models import Category

def home_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home.html', context)
