from django import forms
from allauth.account.forms import SignupForm


class CustomRegistrationForm(SignupForm):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=300)
    phone = forms.CharField(max_length=100, required=False)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Confirm Password")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, request):
        user = super(CustomRegistrationForm, self).save(request)
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.name = self.cleaned_data['name']
        user_profile.email = self.cleaned_data['email']
        user_profile.phone = self.cleaned_data['phone']
        user_profile.save()
        # Set the user's password
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user
