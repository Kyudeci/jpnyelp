from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Food
# Create your views here.
def homepage(request):
    foods = Food.objects.all()
    return render(request, 'jpnyelp/index.html', {'foods':foods})

class HomeView(TemplateView):
    template_name = 'jpnyelp/index.html'
