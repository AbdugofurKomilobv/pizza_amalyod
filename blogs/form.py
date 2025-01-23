from django import forms

from blogs.models import ContactModel



class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['phone_number']


class AboutPageForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['subject']