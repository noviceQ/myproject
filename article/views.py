from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
def home(request):
    postlist = Article.objects.all()
    return render(request,'home.html',{'post_list':postlist})

def detail(request,my_args):
    postObject = Article.objects.all()[int(my_args)]
    postStr = "title = %s,category = %s,date_time = %s , content = %s " % (postObject.title,postObject.category,postObject.date_time,postObject.content)
    return HttpResponse("Your args is get contetn %s" % postStr)
