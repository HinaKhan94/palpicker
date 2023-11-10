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
from offer.models import Post, Request
from django.contrib.auth.models import User


class RegistrationView(CreateView):
    """
    Handles the registration view
    """
    form_class = CustomRegistrationForm
    template_name = 'account/signup.html'

    def form_valid(self, form):
        user = form.save(self.request)
        login(self.request, user)
        return super().form_valid(form)


@login_required
def user_profile(request):
    """
    displays user's dashboard with different crud
    functionailties, it alaos displays
    offers made by the user and requests made
    in the past and present with pending and approved statuses

    """

    # Retrieve the user's requests
    user_requests = Request.objects.filter(user_fk=request.user)

    # Get the user's offers
    user_offers = Post.objects.filter(author=request.user)

    # Paginate the offers
    items_per_page = 3
    paginator_offers = Paginator(user_offers, items_per_page)
    page_number_offers = request.GET.get('page_offers')
    page_offers = paginator_offers.get_page(page_number_offers)

    # Paginate the requests
    paginator_requests = Paginator(user_requests, items_per_page)
    page_number_requests = request.GET.get('page_requests')
    page_requests = paginator_requests.get_page(page_number_requests)

    context = {
        'user': request.user,
        'user_offers': page_offers,
        'user_requests': page_requests,
    }

    return render(request, 'dashboard/user_profile.html', context)
