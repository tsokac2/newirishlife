from django.shortcuts import render
from .models import Life


def life(request):
    """ A view to return the Life template """
    life_section = Life.objects.all()
    template = 'life/life.html'
    context = {
        'life_section': life_section
    }

    return render(request, template, context)