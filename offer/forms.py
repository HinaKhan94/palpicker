from .models import Post, Request, Contact
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
        fields = ['name', 'email', 'message']


class CreateOfferForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Post
        fields = ['title', 'description', 'price',
                  'featured_image', 'excerpt']


class EditOfferForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'featured_image', 'excerpt']
