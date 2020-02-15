from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact
from .newcontact import ContactForm
from django.views import generic


def index(request):
    contacts = Contact.object.all().order_by('firstName')
    return render(request, 'index.html', {'contacts': contacts})


def new(request):
    return render(request, 'new.html')#, {'contact': Contact}


def add(request):
    # if this is a POST request we need to process the form data
    template = 'new.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if Contact.object.filter(mobileNumber1=form.cleaned_data['mobileNumber1']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Phone Number already exists.'
                })
            else:
                # Create the user:

                contact = Contact.object.create_contact(
                    form.cleaned_data['firstName'],
                    form.cleaned_data['lastName'],
                    form.cleaned_data['mobileNumber1'],
                    form.cleaned_data['email'],
                    form.cleaned_data['dateOfBirth']
                )
                contact.save()

                # redirect to index
                return HttpResponseRedirect('../../phonebook')

    # No post data availabe, let's just show the page.
    else:
        form = ContactForm()
    return render(request, 'new.html', {'form': form})


class EditView(generic.edit.UpdateView):
    template_name = 'edit.html'
    model = Contact
    fields = ['id']



def alter(request):
    # if this is a POST request we need to process the form data
    template = 'edit.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if Contact.object.filter(mobileNumber1=form.cleaned_data['mobileNumber1']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Phone Number already exists.'
                })
            else:
                # Create the user:
                contact = Contact.object.get(mobileNumber1=form.cleaned_data['mobileNumber1'])
                contact.firstName = form.cleaned_data['firstName']
                contact.lastName = form.cleaned_data['lastName']
                contact.email = form.cleaned_data['email']
                contact.mobileNumber1 = form.cleaned_data['mobileNumber1']
                contact.dateOfBirth = form.cleaned_data['dateOfBirth']
                contact.save()

                # redirect to index
                return HttpResponseRedirect('../../phonebook')

    # No post data availabe, let's just show the page.
    else:
        form = ContactForm()
    return render(request, 'edit.html', {'form': form})
