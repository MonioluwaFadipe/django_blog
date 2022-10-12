from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

#create about page
def about(request):
    return HttpResponse('<h1>About Blog</h1>') 
