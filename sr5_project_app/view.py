from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


def helloworld(request):
    return HttpResponse("<h1>Hello world</h1>")


def home(request):
    return HttpResponse("<h1>Nang Seakheng</h1>")


def handleContact(request):
    return render(request, "contact.html")


def handleAbout(request):
    return render(request, "about.html")


def masterpage(request):
    return render(request, "app.html")


def homepage(request):
    name = "Sok Phorn is handsome not threesome"
    posts = [
        {
            "author": "Sok Khim",
            "content": "Beautiful girl friends"
        },
        {
            "title": "Enjoy life",
            "author": "Sok Phorn",
        },
        {
            "author": "Sok Vong",
        },
    ]
    return render(request, "homepage.html", {'name': name, "posts": posts})


def welcome(request):
    data = {'posts': Article.objects.all()}
    return render(request, "home.html", data)


def addArticle(request):
    if request.method == 'GET':
        form = ArticleForm()
        data = {'form': form}
        return render(request, "views/forms/add.html", data)
    else:
        data = ArticleForm(request.POST)
        data.save()
        return redirect('dashboard')


def viewDetail(request, id):
    form = ArticleForm()
    data = {'post': Article.objects.get(id=id), 'form': form}
    return render(request, 'views/forms/detail.html', data)


def updateArticle(request, id):
    if request.method == 'GET':
        post = Article.objects.get(id=id)
        form = ArticleForm(instance=post)
        data = {
            'form': form,
            'post': post
                }
        return render(request,'views/forms/update.html',data )
    elif request.method == 'POST':
        post = Article.objects.get(id=id)
        data= ArticleForm(request.POST, instance=post)
        data.save()
        messages.success(request, 'Success updated 😎')
        return redirect('dashboard')
    

def deleteArticle(request, id): 
    if request.method == 'POST':
        post = Article.objects.get(id=id)
        post.delete()
        return redirect('dashboard')
