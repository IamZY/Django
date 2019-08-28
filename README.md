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

  