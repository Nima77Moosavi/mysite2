from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog_view(request, cat=None, author_username=None, tag=None):
    posts = Post.objects.filter(status=True)
    if cat:
        posts = posts.filter(category__name=cat)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if tag:
        posts = posts.filter(tags__name__in=[tag])
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=cat)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        posts = posts.filter(content__icontains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)