from .models import Post, Request, Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
import uuid


class RequestForm(forms.ModelForm):
    """
    handles the information provided
    by the user who is making the request
    for a particular offer. it automatically
    asisgns the user_fk so to display requests
    on the user profile page for user to see
    """
    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'email', 'phone', 'message',)
    # user_fk field is hidden
    user_fk = forms.IntegerField(widget=forms.HiddenInput(), required=False)


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
    takes in all the information required to
    create a new offer
    """
    class Meta:
        model = Post
        fields = ['title', 'description', 'price',
                  'featured_image', 'excerpt']


class EditOfferForm(forms.ModelForm):
    """
    lets the user edit an existinf offer that
    he/she mmade with prepopulated fields with the
    old information
    """
    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'featured_image', 'excerpt']
