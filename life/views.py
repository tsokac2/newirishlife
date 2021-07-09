from django.shortcuts import render


def index(request):
    """ A view to return the life section page """

    return render(request, 'life/life.html')