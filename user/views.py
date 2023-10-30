from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm, UserProfileForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UserProfile
from offer.models import Post


class RegistrationView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('dashboard/user_profile.html')  # Redirect to the user's profile page after registration

    def form_valid(self, form):
        user = form.save(self.request)
        login(self.request, user)
        return super().form_valid(form)



@login_required
def user_profile(request):
    # Retrieve the user's profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Get the user's offers
    user_offers = Post.objects.filter(author_profile=user_profile)

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'user_offers': user_offers,
    }

    return render(request, 'dashboard/user_profile.html', context)


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the user's profile page after editing
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'dashboard/edit_profile.html', context)