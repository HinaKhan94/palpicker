from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Contact
from .forms import RequestForm, ContactForm, CreateOfferForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "requested": False,
                "request_form": RequestForm,
            },
     
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        request_form = RequestForm(data=request.POST)

        if request_form.is_valid():
            request_form.instance.email = request.user.email
            request_form.instance.name = request.user.username
            booking = request_form.save(commit=False)
            booking.post = post
            booking.save()
        else: 
            request_form = RequestForm()
        
    

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "requested": True,
                "request_form": request_form,
            },
     
        )

class AboutView(generic.TemplateView):
    template_name = 'aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'aboutus'
        return context


class ContactView(generic.TemplateView):
    """
    Renders Contact page form and submits user data via email to the
    administrator and to the user.

    Contact view is accessed directly via the Contact link in the menu bar,
    or via the van_detail page.

    If the contact form is accessed directly by the menu bar, the page
    redirects to the home page.

    If the contact form is accessed by the van_detail page, the email includes
    the van details and redirects the user back to the van_detail page
    """
    template_name = 'contact.html'

    def post(self, request, slug=None, *args, **kwargs):
        user = User.objects.get(username='admin')
        post = None

        if slug is not None:
            post = get_object_or_404(Post, slug=slug)

        if request.method == 'POST':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data['name']
                email = contact_form.cleaned_data['email']
                message = contact_form.cleaned_data['message']

            subject = 'Offer Inquiry'
            if post is not None:
                subject += ' ' + post.name

            send_mail(
                subject,
                'There has been an inquiry from: ' + name + ' from email: '
                + email + '. Their message is as follows: "' + message + '." '
                'An administrator will get back to you within 24 hours.',
                'admin@palpicker.com',
                [email, user.email],
                fail_silently=False
            )

            messages.success(request, "Your message has been sent! "
                                      "You will be contacted within 24 hours.")
            
            # Save the submission to the database
            submission = Contact(name=name, email=email, message=message)
            submission.save()
            
            if post is not None:
                return redirect('post_detail', slug=slug)
            else:
                return redirect('home')
        else:
            contact_form = ContactForm()

        context = {
            'post': post,
            'contact_form': contact_form,
            'slug': slug
        }

        return render(request, 'contact.html', context)


class CreateOfferView(View):
    template_name = 'user_profile.html'

    def get(self, request):
        form = CreateOfferForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateOfferForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('user_profile')
        return render(request, self.template_name, {'form': form})