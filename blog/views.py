from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)