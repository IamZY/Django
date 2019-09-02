from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import RedirectView,TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,DeleteView
import datetime
from .forms import RegistrationForm
from .models import User
from django.urls import reverse_lazy

# Create your views here.
def login(request):
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # 验证通过
        if form.is_valid():
            user = User()
            user.name = form.cleaned_data["username"]
            user.password = form.cleaned_data["password1"]
            user.birthday = form.cleaned_data["birthday"]
            user.email = form.cleaned_data["email"]
            user.save()
            return HttpResponseRedirect("/books/list/")
    else:
        form = RegistrationForm()
    return render(request,"registration.html",{"form":form})

def show_list(request):
    # 查询所有数据
    list = User.objects.all()
    return render(request,"show_list.html",{"list":list})

def remove_user(request):
    username = request.GET["username"]
    u = User.objects.get(name=username)
    u.delete()
    return HttpResponseRedirect("/books/list/")


class UserListView(ListView):
    model = User
    ordering = ["name"]
    paginate_by = 1
    # queryset = User.objects.filter(name__contains="tom")


class UserDetailView(DetailView):
    model = User


class RegisrationFormView(FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = "/books/list/"
    def form_valid(self, form):
        user = User()
        user.name = form.cleaned_data["username"]
        user.password = form.cleaned_data["password1"]
        user.birthday = form.cleaned_data["birthday"]
        user.email = form.cleaned_data["email"]
        user.save()
        
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("userList")

# def show_book_info1(request):
#     context = {"book_name":"abc","author":"123"}
#     return render(request,"book.html",context)

# def show_book_info2(request):
#     pass

# def show_book_price1(request,price):
#     info = "abcd"
#     context = {"info":info,"price":float(price)}
#     return render(request,"book_info.html",context)

# def show_book_price2(request,price):
#     info = "abcd"
#     context = {"info":info,"price":price}
#     return render(request,"book_info.html",context)


# def show_book_info(request):
#     print("=================================")
#     book1 = {"bookname":"abc","author":"123"}
#     book2 = {"bookname":"abc","author":"123"}
#     book3 = {"bookname":"abc","author":"123"}
#     list = []
#     list.append(book1)
#     list.append(book2)
#     list.append(book3)
#     return render(request,"book.html",{'list': list})



# class MyView(TemplateView):
#     template_name = "book.html"

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context["book_name"] = "abcf"
#         context["author"] = "123"
#         return context


# def index(request):
#     response = HttpResponse("<h1>设置Cookie</h1>")
#     # 使用max_age设置超时时间：
#     timeoutdate = datetime.datetime.today() + datetime.timedelta(days=10)
#     response.set_cookie('userid', 'tony', expires=timeoutdate)
#     # response.set_cookie("userid","tony")
#     # return render(request,"login.html")
#     return response

# def login(request):
#     if request.method == 'POST':
#         datas = request.POST
#         print(datas["userid"])
#         print(datas["userpwd"])
#         return render(request,"result.html",{"result":datas})
#     else:
#         datas = request.GET
#         print(datas["userid"])
#         print(datas["userpwd"])
#         return render(request,"registration.html")
    

# def hello(request):
#     name = request.COOKIES.get("userid")
#     response = HttpResponse("<h3>hello world</h1>",charset = "gbk")
#     # response.charset = "utf-8"
#     response.write("<h>{0}</h3>".format(name))
#     return response

