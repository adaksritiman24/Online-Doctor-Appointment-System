from django.shortcuts import redirect, render
from datetime import datetime
from django import views
from article.models import Article
from django.db.models import Q
from django.contrib import messages
import random

# Create your views here.
class UploadPage(views.View):

    def get(self,request):
        current_date=datetime.now().date()
        author=request.user
        return render(request, 'article/uploadpage.html', {'date':current_date, 'author':author})
    
    def post(self,request):
        title=request.POST['title']
        date=datetime.now().date()
        blog=request.POST['blog']
        try:
            imagein=request.FILES['imagein']
            article=Article(title=title, upload_date=date, image=imagein, blog=blog)
        except:
            article=Article(title=title, upload_date=date, blog=blog)
        # print(title, date, imagein, blog)
        article.save()
        return redirect('/upload/')

def read(request,id):
    article=Article.objects.get(pk=id)
    return render(request, 'article/blogpage.html', {'article':article})

def home(request):
    articles_list_randomized=list(Article.objects.all())
    article_list_sorted=Article.objects.order_by("-upload_date")[0:4]
    random.shuffle(articles_list_randomized)
    # print(articles_list_randomized)
    return render(request, 'article/articleshome.html', {'articles_last_added':article_list_sorted, 'articles_quick_read':articles_list_randomized[0:6]})
    # return render(request, 'article/articleshome.html', {'articles_last_added':article_list_sorted[0:min(len(article_list_sorted),3)], 'articles_quick_read':article_list_randomized[0:min(len(article_list_randomized),6)]})

def results(request):
    articles_list=Article.objects.order_by("-upload_date")
    return render(request, 'article/results.html', {'articles':articles_list})

def search(request):
    keyword=request.GET['keyword']
    articles_list=Article.objects.all()
    results=articles_list.filter(Q(title__icontains=keyword) | Q(blog__icontains=keyword))
    if(len(results)==0):
        messages.error(request, 'Sorry, found nothing like that')
    return render(request, 'article/results.html', {'articles':results})