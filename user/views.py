from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
#from .models import UserProfile
from offer.models import Post
from django.contrib.auth.models import User


class RegistrationView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'account/signup.html'
    # Redirect to the user's profile page after registration
    success_url = reverse_lazy('dashboard/user_profile.html')

    def form_valid(self, form):
        user = form.save(self.request)
        login(self.request, user)
        return super().form_valid(form)


@login_required
def user_profile(request):
    # Retrieve the user's profile
    #user_profile, created = (
        #User.objects
        #.get_or_create(user=request.user)
    #)

    # Get the user's offers
    user_offers = Post.objects.filter(author=request.user)

    items_per_page = 3
    paginator = Paginator(user_offers, items_per_page)
    page_number = request.GET.get('page')
    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'user_offers': page,
    }

    return render(request, 'dashboard/user_profile.html', context)

