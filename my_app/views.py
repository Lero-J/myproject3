from django.shortcuts import render, redirect

# Create your views here.
from .models import Article
def show_info(request):
    articles = Article.objects.all()
    ctx = {
        'articles': articles
    }
    return render(request, 'index.html', context=ctx)

def show_articles_info(request, article_id):
    article = Article.objects.get(pk=article_id)
    ctx = {
        'info' : article
    }
    return render(request, 'article.html', context=ctx)








