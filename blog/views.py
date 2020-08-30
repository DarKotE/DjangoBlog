from django.shortcuts import render
posts = [

    {
        'author': 'Maxx',
        'title': 'Test Post 1',
        'content': 'Testing text content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'John',
        'title': 'Test Post 2',
        'content': 'Repeat testing text content',
        'date_posted': 'August 28, 2020'
    }

]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html',{'title':'About'})
