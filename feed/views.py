from django.views.generic import ListView
from .models import Post

class HomePage(ListView): # Render out a template with all of the posts
    http_method_names = ["get"] # All user can do is get the page request and view the post
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = "posts" # By default it's called "objects"
    queryset = Post.objects.all().order_by('-id')[0:30] # 30 max posts loaded per page