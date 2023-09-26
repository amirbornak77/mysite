from django import template
from blog.models import Post
register = template.Library()



@register.simple_tag(name='post_count')
def function():
    count = Post.objects.filter(status=1).count()
    return count

@register.simple_tag(name='totallposts')
def function():
    posts = Post.objects.filter(status=1)
    return posts