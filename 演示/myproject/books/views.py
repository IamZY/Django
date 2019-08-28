from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello(request):
    return HttpResponse("<h1>hello world 世界你好</h1>")


# 类基础视图
class MyView(View):
    def get(self,request):
        return HttpResponse("<h1>类基础视图</h1>")