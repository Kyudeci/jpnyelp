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

class HomeView(TemplateView):
    template_name = 'jpnyelp/index.html'
