from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import BookInfo,HeroInfo
from django.views.generic import View
# Create your views here.

# class IndexView(View):
#     def get(self,request):
#         return render(request,"booktest/index.html",{"username":"aaa"})
def index(request):
    # return HttpResponse("这里是首页  <a href='/booktest/list/'>跳转到列表页</a> ")

    temp1=loader.get_template("booktest/index.html")
    result = temp1.render({"name":"lwd"})
    return HttpResponse(result)


def list(request):
    s= """
    <br>
    <a href='/booktest/detail/1/'>跳转到详情页1</a>
    <br>
    <a href='/booktest/detail/2/'>跳转到详情页2</a>
    <br>
    <a href='/booktest/detail/3/'>跳转到详情页3</a>
    """
    # return HttpResponse("这里是列表页 %s "%(s,))
    temp2 = loader.get_template("booktest/list.html")
    books = BookInfo.objects.all()
    result = temp2.render({"books":books})
    return HttpResponse(result)


def detail(request,id):
    # return HttpResponse("这里是s%详情页  <a href='/booktest/list/'>跳转到列表页</a> "%(id,))
    temp3 = loader.get_template("booktest/detail.html")
    book = BookInfo.objects.get(pk=id)
    result = temp3.render({"book":book})
    return HttpResponse(result)

def deletehero(request,id):
    # return render(request)
    # return HttpResponse("hello")

    hero = HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()

    # return HttpResponseRedirect("/booktest/detail/"+str(bookid)+"/")

    return redirect(reverse("booktest:detail",args=(bookid,)))

def addhero(request,id):
    book = BookInfo.objects.get(pk=id)
    if request.method =="GET":
        return render(request,"booktest/addhero.html",{"book":book})
    elif request.method == "POST":
        name = request.POST.get("username")
        content = request.POST.get("content")
        gender = request.POST.get("gender")

        hero = HeroInfo()
        hero.name=name
        hero.content=content
        hero.book=book
        hero.gender=gender
        hero.save()

        return HttpResponse("添加成功")