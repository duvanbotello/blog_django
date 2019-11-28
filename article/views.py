from django.shortcuts import render
from article.models import Article
# Create your views here.
def ver_post(request, id):
    article = Article.objects.filter(id=id).first()
    return render(request, "article/article.html", {'article': article})    