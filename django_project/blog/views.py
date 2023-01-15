from django.shortcuts import render

posts = [
    {
        'author': 'Vardges',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 15, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 15, 2023'
    }
]


def home(request):
    context = {
        "users": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
