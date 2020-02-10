from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.all().order_by('firstName')
    return render(request, 'index.html', {'contacts': contacts})


def new(request):
    return render(request, 'new.html', {'contact': Contact})


def add(request):
    return render('phonebook:index')