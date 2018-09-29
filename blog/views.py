from django.shortcuts import render
from django.http import HttpResponse

# Some Dummy Post

posts=[
    {
        'author':'Sohel Ahmed',
        'title':'This is Post 1',
        'content':'Post 1 Content',
        'date_posted':'12 Aug 2018'
    },
    {
        'author':'Sohel Ahmed',
        'title':'This is Post 2',
        'content':'Post 2 Content',
        'date_posted':'12 Aug 2018'
    },
    {
        'author':'Shakil Ahmed',
        'title':'This is Post 1 From Shakil',
        'content':'Post 1 Content of Shakil',
        'date_posted':'12 Aug 2018'
    }
]

# Create your views here.

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')