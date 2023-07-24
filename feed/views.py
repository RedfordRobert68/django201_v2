from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Post

class HomePage(ListView): # Render out a template with all of the posts
    http_method_names = ["get"] # All user can do is get the page request and view the post
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = "posts" # By default it's called "objects"
    queryset = Post.objects.all().order_by('-id')[0:30] # 30 max posts loaded per page

class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post" # Change name to match model

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html" # View more about create view at ccbv.co.uk
    fields = ["text"]
    success_url = "/"

    def post(self, request, *args, **kwargs):
        post = Post.objects.create(
            text=request.POST.get("text"),
            author=request.user,
        )

        return render(
            request, # Always takes request as it's first render
            "includes/post.html",
            {
                "post":post,
                "show_detail_link":True, 
            },
            content_type="application/html"
        )

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user # Needs to be thrown into dispatch
        obj.save()
        return super().form_valid(form)