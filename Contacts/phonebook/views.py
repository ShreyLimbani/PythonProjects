from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact
from .newcontact import ContactForm


def index(request):
    contacts = Contact.object.all().order_by('firstName')
    return render(request, 'index.html', {'contacts': contacts})


def new(request):
    return render(request, 'new.html', {'contact': Contact})


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
