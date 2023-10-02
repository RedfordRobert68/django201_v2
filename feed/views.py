from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from followers.models import Follower
from .models import Post

class HomePage(TemplateView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            following = list(
                Follower.objects.filter(followed_by=self.request.user).values_list('following', flat=True)
            )
            # if following:
            #     # Show the default 30
            #     posts = Post.objects.all().order_by('-id')[0:60]
            # else:
            posts = Post.objects.all().order_by('-id')[0:60]

        else:
            posts = Post.objects.all().order_by('-id')[0:30]
            
        context['posts'] = posts
        return context
    
class FriendsPage(TemplateView): # Render out a template with all of the posts
    http_method_names = ["get"] # All user can do is get the page request and view the post
    template_name = "feed/friends_post.html"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['is_following'] = Follower.objects.filter(following=self.request.user).exists()
        if self.request.user.is_authenticated:
            following = list(
                Follower.objects.filter(followed_by=self.request.user).values_list('following', flat=False)
            )
            posts = Post.objects.filter(author__in=following).order_by('id')
        context['posts'] = posts
        return context


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

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user # Needs to be thrown into dispatch
        obj.save()
        return super().form_valid(form)

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