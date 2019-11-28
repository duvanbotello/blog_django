from django.shortcuts import render
from article.models import Article
# Create your views here.

def home(request):
    articles = Article.objects.all()[:5]
    return render(request, "home/home.html", {'articles': articles})    