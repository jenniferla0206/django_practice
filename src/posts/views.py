from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>create<h1>")

def post_detail(request):
    context = {
        'title': 'Detail'
    }
    return render(request, 'index.html', context)
    #return HttpResponse("<h1>detail<h1>")

def post_list(request):
    '''if request.user.is_authenticated():
        context = {
            'title': 'my user list'
        }
    else:
        context = {
            'title': 'List'
        }'''
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List'
    }
    return render(request, 'index.html', context)
    #return HttpResponse("<h1>list<h1>")

def post_update(request):
    return HttpResponse("<h1>update<h1>")

def post_delete(request):
    return HttpResponse("<h1>delete<h1>")
