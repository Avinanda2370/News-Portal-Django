from django.http import HttpResponse
from django.shortcuts import render

from news.models import News
# Create your views here.
def first(request):
    news = News.objects.all()
    context = {
        'mynews' : news,
    }
    return render(request,'news/index.html',context)

def singleview(request,pk):
    news = News.objects.get(id = pk)
    context = {
        "news" : news,
    }
    return render(request,'news/singleview.html',context)

def catview(request):
    categoryname = request.GET.get('category')
    my_data = News.objects.filter(category__slug=category_name)
    context = {
        "newses": my_data,
    }
    return render(request,'news/categoryview.html')