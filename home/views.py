from django.shortcuts import render
from .models import Home

def index(request):
    """ A view to return the Home index page """
    hello_section = Home.objects.all()
    template = 'home/home.html'
    context = {
        'hello_section':hello_section
    }

    return render(request, template, context)