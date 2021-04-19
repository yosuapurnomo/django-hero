from django.shortcuts import render
from nama.models import namaModel

def mainView(request):
    objects = namaModel.objects.all()
    context = {}
    context['object'] = objects
    return render(request, 'index.html', context)