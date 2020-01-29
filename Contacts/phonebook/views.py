from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    #c = Contact.objects.
    return render(request, 'index.html', {'contacts': contacts})


def add(request):
    return render(request, 'add.html', {'contact': Contact})
