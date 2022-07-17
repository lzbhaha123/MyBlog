from turtle import pos
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category,Post,Skill,Profile,Referee

categories = Category.objects.all().order_by('category_order')

def index(request):
    posts = {}
    
    for c in categories:
        posts[c.id] = Post.objects.filter(category=c).order_by('-id')[:3]

    return render(request, 'cv/index.html', {'categories':categories,'posts':posts})

def posts(request,category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)

    return render(request, 'cv/posts.html',{'category':category,'posts':posts,'nav':categories})

def detail(request,post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'cv/detail.html',{'post':post,'nav':categories})

def about(request):
    skills = Skill.objects.all()
    profile = Profile.objects.get(id = 1)
    referees = Referee.objects.all().order_by('-id')
    return render(request, 'cv/about.html',{'skills':skills,'profile':profile,'nav':categories,'referees':referees})