from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages


# Create your views here.

@login_required(login_url='login')
def user_profile(request, pk):
    '''
    A view that renders user's profile
    '''
    profile = UserProfile.objects.get(id=pk)
    

    context = {
        'profile': profile,
        
    }
    return render(request, 'user/user_profile.html', context)

