from django.shortcuts import render


def index(request):
    """ A view to return the Trip page """

    return render(request, 'trip/trip.html')