from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo,HeroInfo
# Create your views here.

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