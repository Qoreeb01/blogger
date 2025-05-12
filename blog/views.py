from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def news(request):
    return render(request, 'news.html', {})

def business(request):
    return render(request, 'business.html', {})

def politics(request):
    return render(request, 'politics.html', {})

def sport(request):
    return render(request, 'sport.html', {})