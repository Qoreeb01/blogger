from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def register(request):
    if request.mmethod == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm
        return render(request, 'registration/register.html', {'form': form})

def home(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'index.html', {'full_post': full_post})

def news(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'news.html', {'full_post': full_post})


def business(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'business.html', {'full_post': full_post})

def politics(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'politics.html', {'full_post': full_post})


def sport(request):
    full_post = Post.objects.all().order_by('-created_on')
    return render(request, 'sport.html', {'full_post': full_post})

def post_detail(request, slug):
    f_post = get_object_or_404(Post, slug=slug)
    comments = Post.comments.all().order_by('-created_on')
    return render(request, 'post.detail', {'f_post': f_post})


    if request.method == 'POST':
      form = CommentForm(request.POST)
    



    else:
       form = CommentForm()

    return render(request, 'post_detail.html', 
                  {'f_post': f_post,
                   'comments': comments,
                   'form': form})


