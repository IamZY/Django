from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import RedirectView,TemplateView

# Create your views here.

def show_book_info1(request):
    context = {"book_name":"abc","author":"123"}
    return render(request,"book.html",context)

def show_book_info2(request):
    pass

def show_book_price1(request,price):
    info = "abcd"
    context = {"info":info,"price":float(price)}
    return render(request,"book_info.html",context)

def show_book_price2(request,price):
    info = "abcd"
    context = {"info":info,"price":price}
    return render(request,"book_info.html",context)


def show_book_info(request):
    print("=================================")
    book1 = {"bookname":"abc","author":"123"}
    book2 = {"bookname":"abc","author":"123"}
    book3 = {"bookname":"abc","author":"123"}
    list = []
    list.append(book1)
    list.append(book2)
    list.append(book3)
    return render(request,"book.html",{'list': list})



class MyView(TemplateView):
    template_name = "book.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["book_name"] = "abcf"
        context["author"] = "123"
        return context