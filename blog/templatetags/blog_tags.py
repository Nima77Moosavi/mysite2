from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag
def posts():
    posts = Post.objects.filter(status=True)
    return posts

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts():
    latestposts = Post.objects.filter(status=True).order_by('published_date')
    return {'latestposts':latestposts}

@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    category_dict = {}
    for category in categories:
        category_dict[category] = posts.filter(category=category).count()
        
    return {'categories': category_dict}