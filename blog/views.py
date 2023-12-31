from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name="accounts/login.html")
def blog_view(request,**kwargs):
    current_time = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=current_time)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name']) 
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in= [kwargs['tag_name']])
        
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    current_time = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=current_time)
    post = get_object_or_404(posts, pk=pid)
    post.counted_views += 1
    post.save()
    next_post =  posts.filter(id__gt = post.id).order_by('id').first()
    previous_post = posts.filter(id__lt=post.id).order_by('-id').first()
    
    context = {
        'post': post,
        'next_post': next_post, 
        'previous_post': previous_post,
        }
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)



