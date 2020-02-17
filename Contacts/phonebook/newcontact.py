from django import forms


class ContactForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    countryCode1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobileNumber1 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    dateOfBirth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))