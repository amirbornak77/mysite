from django.urls import path
from blog.views import *

app_name = "blog"
urlpatterns = [
    path('',blog_view, name='index'),
    path('<int:pid>',blog_single, name='single'),
    path('', list_posts, name='list_posts'),
    # path('post-<int:pid>',test_view, name='test'),
    
]