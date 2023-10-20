from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import RequestForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


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