from django.shortcuts import render

def index(request):
    """ A view to return the Home index page """

    return render(request, 'home/home.html')