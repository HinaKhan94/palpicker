from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


from .models import UserProfile
from .forms import UserProfileForm

from offer.models import Post

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_profile')  # Redirect to the user profile page after successful login

    # Add handling for unsuccessful login here
    return render(request, 'account/login.html')


@login_required
def profile(request):
    """
    Display a user's profile Page
    """
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
    except UserProfile.DoesNotExist:
        # If the user doesn't have a UserProfile, redirect to the signup page.
        return redirect('account_signup')  # Redirect to the signup view or URL

   
    else:
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile was updated successfully')
            else:
                messages.error(request, 'Profile update failed. Please ensure your profile information is valid and try again.')
        else:
            form = UserProfileForm(instance=profile)

        # Query related posts for the valid user profile
        posts = Post.objects.filter(author=request.user).order_by('-updated_on')

        template = 'dashboard/user_profile.html'
        context = {
            'form': form,
            'posts': posts,
            'on_profile_page': True
        }

        return render(request, template, context)