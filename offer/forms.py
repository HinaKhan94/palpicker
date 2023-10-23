from .models import Request
from django import forms

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'email', 'message',)

class ContactForm(forms.Form):
    """
    It is used on the contact page for any user
    queries
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