from .models import Request
from django import forms

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'email', 'message',)