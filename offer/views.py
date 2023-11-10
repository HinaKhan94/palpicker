from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from .models import Post, Contact, Request
from .forms import RequestForm, ContactForm, CreateOfferForm, EditOfferForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.http import Http404


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    his view handles both GET and POST
    requests for a specific Post. In the case of a
    GET request, it displays the details of the
    Post along with a form for making a request.
    In the case of a POST request, it processes
    the form submission, creating a new Request
    associated with the Post.

    """
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


class CreateRequestView(LoginRequiredMixin, CreateView):
    """
    the view for creating requests
    his view ensures that the user_fk
    field of the newly created request
    is set to the current user before saving the request.

    """
    model = Request
    form_class = RequestForm
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def form_valid(self, form):
        print("Form is valid")
        post = self.get_object()
        form.instance.post = post
        form.instance.user_fk = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def get_success_url(self):
        success_url = reverse('user_profile')
        print("Success URL:", success_url)
        return success_url


class ContactView(View):
    """
    saves contact form data in the Contact model
    when the form is submitted successfully.

    """
    template_name = 'contact.html'

    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, self.template_name, context)

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Your message has been sent! "
                             "You will be contacted within 24 hours.")
            return redirect('home')
        else:
            messages.error(request, "There was an error "
                           "in your submission. Please try again.")
            # Redirects to the contact page in case of an error
            return redirect('contact')


class CreateOfferView(View):
    """
    creates a new offer for the user with the
    fields shown to the user for a successful
    offer creation

    """
    template_name = 'dashboard/create_offer.html'

    @method_decorator(login_required)
    def get(self, request):
        form = CreateOfferForm()
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = CreateOfferForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            # success message
            messages.success(request,
                             'Your request has been sent for approval.')

            return redirect('user_profile')
        return render(request, self.template_name, {'form': form})


class DeleteOfferView(LoginRequiredMixin, View):

    """
    This view first checks if the user is the author of the offer
    and whether the offer exists. If not,
    it raises a 404 error. If it's a POST request,
    the offer is deleted. Otherwise, it renders the
    delete confirmation template.

    """

    template_name = 'dashboard/delete_offer.html'

    def get(self, request, offer_slug):
        try:
            offer = Post.objects.get(slug=offer_slug)
            if offer.author != request.user:
                raise Http404
        except Post.DoesNotExist:
            raise Http404

        return render(request, self.template_name, {'offer': offer})

    def post(self, request, offer_slug):
        try:
            offer = Post.objects.get(slug=offer_slug)
            if offer.author != request.user:
                raise Http404
        except Post.DoesNotExist:
            raise Http404

        offer.delete()
        messages.success(request, 'Offer deleted successfully')
        return redirect('user_profile')


class EditOfferView(LoginRequiredMixin, View):
    """
     allows you to edit the details of an offer using a modal.
     the field are prepopulated with the
     old information

    """
    template_name = 'dashboard/edit_offer.html'

    def get(self, request, offer_slug):
        post = Post.objects.get(slug=offer_slug)
        form = EditOfferForm(instance=post)
        return render(request, self.template_name,
                      {'form': form, 'post': post})

    def post(self, request, offer_slug):
        post = Post.objects.get(slug=offer_slug)
        form = EditOfferForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        return render(request, self.template_name,
                      {'form': form, 'post': post})
