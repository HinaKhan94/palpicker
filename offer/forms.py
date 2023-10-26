from .models import Request, Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
import uuid


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'email', 'message',)

class ContactForm(forms.ModelForm):
    """
    It is used on the contact page for any user
    queries
    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)


    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'message',
        )
    """
