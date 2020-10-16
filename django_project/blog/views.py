from django.shortcuts import render

posts = [
    {
        'author': 'Jason Turner',
        'title': 'Blog Post 1',
        'summary': 'First Post summary',
        'date_posted': 'June 1, 2020'
    },
    {
        'author': 'Jason Turner',
        'title': 'Blog Post 2',
        'summary': 'Second Post summary',
        'date_posted': 'June 2, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


    