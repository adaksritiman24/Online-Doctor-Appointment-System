
from django.shortcuts import redirect, render
from datetime import datetime
from django import views
from article.models import Article
from django.db.models import Q
from django.contrib import messages
import random
from accounts.models import Patient, Doctor

#check whether doctor
def is_Doctor(id):
    try:
        doctor = Doctor.objects.get(pk = id)
        return True
    except Exception:
        return False    

# Create your views here.
class UploadPage(views.View):

    def get(self,request):

        if(request.user.is_authenticated):
            if(is_Doctor(request.user.id)):
                current_date=datetime.now().date()
                author_id=request.user.id
                author = Doctor.objects.get(pk=author_id)

                return render(request, 'article/uploadpage.html', {'date':current_date, 'author':author})
            else:
                messages.error(request, "cannotwrite")
                return redirect("/articles/home/")
        return redirect("/accounts/login/doctor/")            
            
    def post(self,request):
        title=request.POST['title']
        date=datetime.now().date()
        blog=request.POST['blog']
        doctor = Doctor.objects.get(pk = request.user.id)
        try:
            imagein=request.FILES['imagein']
            article=Article(author=doctor, title=title, upload_date=date, image=imagein, blog=blog)
        except:
            article=Article(author=doctor, title=title, upload_date=date, blog=blog)
        # print(title, date, imagein, blog)
        article.save()
        return redirect('/articles/upload/')

def read(request,id):
    article=Article.objects.get(pk=id)
    return render(request, 'article/blogpage.html', {'article':article})

def home(request):
    print("Home called")
    articles_list_randomized=list(Article.objects.all())
    article_list_sorted=Article.objects.order_by("-id")[0:4]
    random.shuffle(articles_list_randomized)
    # print(articles_list_randomized)
    print("Herexxxx")
    return render(request, 'article/articleshome.html', {'articles_last_added':article_list_sorted, 'articles_quick_read':articles_list_randomized[0:6]})
    # return render(request, 'article/articleshome.html', {'articles_last_added':article_list_sorted[0:min(len(article_list_sorted),3)], 'articles_quick_read':article_list_randomized[0:min(len(article_list_randomized),6)]})

def results(request):
    articles_list=Article.objects.order_by("-upload_date")
    return render(request, 'article/results.html', {'articles':articles_list})

def search(request):
    keyword=request.GET['keyword']
    articles_list=Article.objects.all()
    results=articles_list.filter(Q(title__icontains=keyword) | Q(blog__icontains=keyword) | Q(author__first_name__icontains=keyword))
    if(len(results)==0):
        messages.error(request, 'Sorry, found nothing like that')
    return render(request, 'article/results.html', {'articles':results})



def show_home(request):
    if not request.user.is_authenticated:
        return redirect("/")
    else:
        if(is_Doctor(request.user.id)):
            return redirect("/doc")    
        return redirect("/")

def edit_profile(request):
    if(is_Doctor(request.user.id)):
        return redirect("/edit/doctor/")
    else:
        return redirect("/edit/patient/")

def app_page(request):
    if(is_Doctor(request.user.id)):
        return redirect("/appointments/doctor/")
    else:
        return redirect("/appointments/patient/")

# def home_page(request):
#     redirect("/")

def dashboard(request):
    if(is_Doctor(request.user.id)):
        return redirect("/dashboard/doctor/")
    else:
        return redirect("/dashboard/patient/")    
