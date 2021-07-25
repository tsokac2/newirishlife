from django.shortcuts import render
from .models import Work


def work(request):
    """ A view to return the Work template """
    work_section = Work.objects.all()
    template = 'work/work.html'
    context = {
        'work_section': work_section
    }

    return render(request, template, context)
    



