from django.shortcuts import render
from .models import Trip


def trip(request):
    """ A view to return the Trip template """
    trip_section = Trip.objects.all()
    template = 'trip/trip.html'
    context = {
        'trip_section': trip_section
    }

    return render(request, template, context)