from django.shortcuts import render

posts = [
    {
        'author': 'SChege',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'SChege',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})