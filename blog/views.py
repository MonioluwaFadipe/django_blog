from django.shortcuts import render

posts = [
    {
        'author': 'FadipeMD',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 13, 2022'
    },
    {
        'author': 'OniET',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 15, 2022'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

#create about page
def about(request):
    return render(request, 'blog/about.html')
