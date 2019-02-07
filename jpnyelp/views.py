from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Food
# Create your views here.
def homepage(request):
    foods = Food.objects
    return render(request, 'food/index.html', {'foods':foods})

class HomeView(TemplateView):
    template_name = 'index.html'
