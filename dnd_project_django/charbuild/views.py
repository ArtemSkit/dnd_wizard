from django.shortcuts import render
# from django.http import HttpResponse
from .models import Character

# Create your views here.


def index(request):
    # return HttpResponse('Hello from charbuild')
    chars = Character.objects.all()[:10]
    context = {
        'title': 'Value passed to the render as an attribute',
        'chars': chars
    }
    return render(request, 'charbuild/index.html', context)


def details(request, id):
    char = Character.objects.get(id=id)
    context = {
        'char': char
    }
    return render(request, 'charbuild/details.html', context)
