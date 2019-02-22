from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Food
from .models import Dessert
# Create your views here.
def homepage(request):
    foods = Food.objects
    desserts = Dessert.objects
    return render(request, 'jpnyelp/index.html', {'foods':foods, 'desserts':desserts})
def dessert(request):
    desserts = Dessert.objects
    return render(request, 'jpnyelp/dessert.html', {'desserts':desserts})
def appetizer(request):
    foods = Food.objects
    return render(request, 'jpnyelp/appetizer.html', {'foods':foods})

class HomeView(TemplateView):
    template_name = 'jpnyelp/index.html'
    template_name2 = 'jpnyelp/dessert.html'
    template_name3 = 'jpnyelp/appetizer.html'
