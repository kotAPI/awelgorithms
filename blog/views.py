from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Blog

def listQuestions(request):
    latest_blogs = Blog.objects.order_by('-created')[:5]
    context = {
        'latest_blogs': latest_blogs,
    }
    return render(request,'blog/list.html',context)

def detail(request,blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'blog/detail.html', {'blog': blog})