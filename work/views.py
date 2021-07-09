from django.shortcuts import render


def index(request):
    """ A view to return the Work page """

    return render(request, 'work/work.html')


