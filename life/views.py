from django.shortcuts import render


def index(request):
    """ A view to return the Life page """

    return render(request, 'life/life.html')