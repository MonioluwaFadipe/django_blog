from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#create about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
