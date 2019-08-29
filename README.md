# Django
## 创建项目

```shell
django-admin startprotect myproject
```

+ 启动项目

  ```shell
  python manage.py runserver
  ```

+ 更新数据库配置

  ``` 
  python manage.py migrate
  ```

## 创建应用程序

```shell
python manage.py startapp books
```

## 视图

+ views.py

  函数视图

  ```python
  from django.shortcuts import render
  from django.http import HttpResponse
  
  # Create your views here.
  def hello(request):
      return HttpResponse("<h1>hello world 世界你好</h1>")
  
  ```

  类基础视图

  ```python
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
  ```

+ 在project中添加映射 urls.py

  ```python
  from django.contrib import admin
  from django.urls import path
  
  urlpatterns = [
      path("books/", include("books.urls"))
      path('admin/', admin.site.urls),
  ]
  ```

+ 在应用程序中创建urls文件

  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path("hello/",views.hello,name = "hello")
      # 类基础视图
      path("myview/",views.MyView.as_view(),name = "myview")
  ]
  ```

## 路径映射

+ urls.py

  ```python
  from django.urls import path,re_path
  from . import views
  
  urlpatterns = [
      path("hello/",views.hello,name = "hello"),
      path("myview/",views.MyView.as_view(),name = "myview"),
      re_path("^id/(?P<book_id>[a-zA-Z0-9]{4})/$",views.show_book_id),
      re_path("^(?P<price>\d+\.\d+)/$",views.show_book_price)
  ]
  ```

+ views.py

  ```python
  def show_book_id(request,book_id):
      s = "<h1>您选择的图书的编号{0}</h1>".format(book_id)
      return HttpResponse(s)
  
  def show_book_price(request,price):
      s = "<h1>您选择的图书的价格{0}</h1>".format(price)
      return HttpResponse(s)
  ```

## 路径转换器

+ 预定义路径转换器：
  + str：匹配除路径分隔符（/）之外的任何非空字符串。
  + int：匹配零或任何正整数。返回一个int。
  + slug：匹配由ASCII字母或数字组成的任何字符串，然后这些字符串可以通过连字符（-）和下划线字符（_）连接。例如， building-your-1st-django-site。
  + uuid：匹配格式化的UUID。必须包含连字符（-），并且字母必须为小写。例如，075194d3-6885-417e-a8a8-6c931e272f00。
  + path：匹配任何非空字符串，包括路径分隔符（/）。 

+ urls.py

  ```python
  urlpatterns = [
      path('hello1/<str:name>/', views.hello1, name='hello'),
      path('hello2/<slug:name>/', views.hello2),
      path('hello3/<uuid:name>/', views.hello3),
      path('hello4/<path:name>/', views.hello4),
      path('<int:book_id>/', views.show_book_id),
  ]
  ```

+ views.py

  ```python
  def hello1(request,name):
      s = "<h1>hello1 {0}</h1>".format(name)
      return HttpResponse(s)
  
  def hello2(request,name):
      s = "<h1>hello2 {0}</h1>".format(name)
      return HttpResponse(s)
  
  def hello3(request,name):
      s = "<h1>hello3 {0}</h1>".format(name)
      return HttpResponse(s)
  
  def hello4(request,name):
      s = "<h1>hello4 {0}</h1>".format(name)
      return HttpResponse(s)
  
  def show_book_id(request,book_id):
      s = "<h1>show_book_id {0}</h1>".format(book_id)
      return HttpResponse(s)
  ```

## 重定向

+ urls.py

  ```python
  from django.urls import path,re_path
  from . import views
  
  urlpatterns = [
      path("hello/",views.hello,name = "hello"),
      path("myview/",views.MyView.as_view(),name = "myview"),
      re_path("^id/(?P<book_id>[a-zA-Z0-9]{4})/$",views.show_book_id),
      re_path("^(?P<price>\d+\.\d+)/$",views.show_book_price,name="book_price"),
      path("info/",views.show_book_info,name = "book_info"),
      path("redirect/",views.MyRedirectView.as_view(),name = "myRedirectView"),
  ]
  ```

+ views.py

  ```python
  from django.shortcuts import render,redirect
  from django.http import HttpResponse
  from django.views import View
  from django.views.generic import RedirectView
  
  # Create your views here.
  def hello(request):
      # return HttpResponse("<h1>hello world 世界你好</h1>")
      # 跳转外部网址
      # return redirect("http://www.baidu.com")
      pass
  
  def show_book_id(request,book_id):
      # s = "<h1>您选择的图书的编号{0}</h1>".format(book_id)
      price = 50.89
      if book_id == 1234:
          price = 80.88
      return redirect("book_price",price = price)
  
  def show_book_price(request,price):
      s = "<h1>您选择的图书的价格{0}</h1>".format(price)
      return HttpResponse(s)
  
  def show_book_info(request):
      return HttpResponse("book_info")
  
  class MyRedirectView(RedirectView):
      pattern_name = "book_info"
  ```

## 模板

+ 注册应用

  在项目目录下`setting.py`

  ```python
  INSTALLED_APPS = [
      'books.apps.BooksConfig'
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

+ 模板

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

+ 创建模板（在books应用下创建templates文件夹用于存放模板）

  + 模板

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>模板</title>
    </head>
    <body>
        <h3>书名 :{{ book_name }}</h3>
        <h3>作者 :{{ author }}</h3>
    </body>
    </html>
    ```

  + views.py

    ```python
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
    
    class MyView(TemplateView):
        template_name = "book.html"
    
        def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            context["book_name"] = "abcf"
            context["author"] = "123"
            return context
    ```

  + urls.py

    ```python
    from django.urls import path,re_path
    from . import views
    
    urlpatterns = [
      path("info1/",views.show_book_info1),
      path("info2/",views.show_book_info2),
      path("myview/",views.MyView.as_view(),name = "myview"),
    ]
    ```

+ 过滤器

  ```html
  <html>
  <body>
      <h3>name变量：{{ name }}</h3>
      <h3>name单词首字母大写：{{ name|title }}</h3>
      <h3>name小写：{{ name|lower }}</h3>
      <h3>name大写：{{ name|upper }}</h3>
      <h3>name字符串长度：{{ name|length }}</h3>
      <h3>获得第一个元素：{{ message|first }}</h3>
      <h3>获得最后一个元素：{{ message|last }}</h3>
      <h3>将元素连接起来：{{ message|join:"&nbsp;&nbsp;" }}</h3>
      <h3>截取前两个单词：{{ message|first|truncatewords:2 }}</h3>
      <h3>日期格式化：{{ date|date:"Y-m-d" }}</h3>
      <h3>数字格式化：{{ number|floatformat:2 }}</h3>
  </body>
  </html>
  ```

+ 模板标签
  标签可以执行一些操作语句，如if、for和模板继承等。
  {% ... %} 

  例如：
  判断结构:
  {% if 条件表达式 %} 
  ...
  {% endif %} 
  循环结构:
  {% for item in 序列 %} 
  ...
  {% endfor %} \

+ 模板继承
   定义基础模板base.html：

  <div id="content">
      {% block body %}
      {% endblock %}
  </div>
  继承基础模板login.html：
  {% extends "base.html" %}
  ...
  {% block body %}
    <table width="40%" border="0">
     ...
    </table>
  {% endblock %} 



















