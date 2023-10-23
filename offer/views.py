from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Contact
from .forms import RequestForm, ContactForm
from django.core.mail import send_mail


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


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/contact_form.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the submission to the database
            submission = Contact(name=name, email=email, message=message)
            submission.save()

            # Send an email
            subject = 'Contact Form Submission'
            message_body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            from_email = 'admin@palpicker.com'

            send_mail(subject, message_body, from_email, [email], fail_silently=False)


            # Redirect to a success page or render a thank-you message
            return redirect('')

        else:
            form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})