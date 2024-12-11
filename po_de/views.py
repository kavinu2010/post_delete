from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
   postii=Post.objects.all()
   return request(render, 'home.html',{'postii':postii})

# def post(request):
#   if request.method=='POST':
