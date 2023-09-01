from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    return HttpResponse("<h1>this is home page</h1>")

def about_view(request):
    return HttpResponse("<h1>This is about page!</h1>")

def contact_view(request):
    return HttpResponse("<h1>This is contact page!!</h1>")