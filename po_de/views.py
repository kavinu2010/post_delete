from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
   postii=Post.objects.all()
   return render(request, 'home.html',{'postii':postii})
 
def posts(request):
   if request.method=='POST':
      postts=PostForm(request.POST)
      if postts.is_valid():
         postts.save()
         return redirect('home')
      
   else :
      postts=PostForm()
   return render(request, 'postt.html',{'postts':postts})


 