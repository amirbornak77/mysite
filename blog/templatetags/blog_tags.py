from django import template
from blog.models import Post
from blog.models import Category
register = template.Library()


# This is for counting the number of posts
@register.simple_tag(name='post_count')
def function():
    count = Post.objects.filter(status=1).count()
    return count
# This is for showing 
@register.simple_tag(name='totallposts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...' 

@register.inclusion_tag('blog/blog-popular-posts.html')
def latesposts():
    posts = Post.objects.filter(status=1).order_by('published_date') 
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-category-widget.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {} 
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}