from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
  posts=Post.objects.all().order_by('fch_publicacion')
  return render(request, "index.html",{'posts':posts} )

def posts(request):
  posts=Post.objects.all().order_by('fch_publicacion')
  return render(request, "posts.html",{'posts':posts})
