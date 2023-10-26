from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'phone',)
        exclude = ('user',)

def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated
    labels and set autofocus on the first field,
    add aria labels to fields for accessibility
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'name': 'Full Name',
        'phone': 'Phone Number',
    }

    self.fields['name'].widget.attrs['autofocus'] = True
    self.fields['name'].widget.attrs['aria-label'] = 'Full Name'
    self.fields['phone'].widget.attrs['aria-label'] = 'Phone Number'

    for field in self.fields:
        if field != 'name':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
        self.fields[field].label = False

