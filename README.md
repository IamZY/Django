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

## 访问静态文件

+ 配置步骤：
  1、确认settings.py中INSTALLED_APPS否安装了django.contrib.staticfiles。
  2、确认settings.py中STATIC_URL的配置：
  STATIC_URL = '/static/'
  3、在books下面创建static文件夹，然后把静态文件复制到static文件夹中。

```html
<!doctype html>
{% load static %}
<html>
<head>
<meta charset="utf-8">
<title>图书管理系统-用户登录</title>
<link rel="stylesheet" type="text/css" href="{% static 'css/book.css' %}">
</head>

<body>
<!-- 页面头部信息 -->
<div id="header">
    <img src="{% static 'images/book_img2.jpg' %}" width="20px" height="20px">
    用户登录
    <hr/>
</div>

<!-- 页面底部信息 -->
<div id="footer">
  <hr/>
  Copyright © 智捷课堂 2008-2018. All Rights Reserved 
</div>

</body>
</html>
```

## HttpRequest请求对象

```html
<!doctype html>
{% load static %}
<html>
<head>
<meta charset="utf-8">
<title>图书管理系统-用户登录</title>
<link rel="stylesheet" type="text/css" href="{% static 'css/book.css' %}">
</head>

<body>
<!-- 页面头部信息 -->
<div id="header">
    <img src="{% static 'images/book_img2.jpg' %}" width="20px" height="20px">
    用户登录
    <hr/>
</div>
<!-- 页面内容信息 -->
<form action="/books/login/" method="POST">
  {% csrf_token %}
  <div id="content">
    <table width="40%" border="0">
      <tbody>
        <tr>
          <td>用户ID：</td>
          <td><input type="text" name = "userid"/></td>
        </tr>
        <tr>
          <td>密码：</td>
          <td><input type="password" name = "userpwd"/></td>
        </tr>
        <tr align="center">
          <td colspan="2">
            <input type="submit" value="确定">
            <input type="reset" value="取消">
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</form>

<!-- 页面底部信息 -->
<div id="footer">
  <hr/>
  Copyright © 智捷课堂 2008-2018. All Rights Reserved 
</div>

</body>
</html>
```

## Cookie

```python
# 设置示例：
def index(request):
    response = HttpResponse("<h3>设置Cookies</h3>")
    # 设置Cookies
    response.set_cookie('userid', 'tony')
    return response
# 使用expires设置超时时间：
timeoutdate = datetime.today() + timedelta(days=10)
response.set_cookie('userid', 'tony', expires=timeoutdate)
# 使用max_age设置超时时间：
response.set_cookie('userid', 'tony', max_age=60)
 
# 2、获取Cookie，使用HttpRequest的COOKIES属性返回Cookie对象，再通过Cookie键获得：
def hello(request):
    # 取出Cookies
    name = request.COOKIES.get('userid')
    response = HttpResponse("<h3>取出Cookies</h3>")
    response.write('<h3>Cookies中userid：' + str(name) + '</h3>')
    return response
```

## Session

Session与Cookie不同，Session是存储在服务器端，服务器为每一个客户端分配一个Session ID，当浏览器关闭或Session操作超时，Session就会失效。Session往往用来存储用户的登录信息。Session数据结构与Cookie一样都是字典结构。

在Django中Session的数据是放到数据库中的，因此需要保证Session表已经创建，如果没有需要执行如下指令：

> python manage.py migrate
>
> 否则发生错误：{OperationalError}no such table: django_session 

+ 设置关闭浏览器Session过期

  >  SESSION_EXPIRE_AT_BROWSER_CLOSE = True

+ 设置Session：

  ```python
  def login(request):
      if request.method == 'POST':
          userid = request.POST['userid']
          request.session['userid'] = userid
      return render(request, 'result.html')
  ```

+ 获取Session：

  ```html
  <h3>
      存储在Session中的userid数据：{{ request.session.userid }}
  </h3>
  ```

  注意：在模板中取Session数据，不能通过方法和下标（session['userid']）方法。方法Session的表达式是session.key，例如：(session.userid)。

+ 删除Session：

  ```python
  def logout(request):
      if request.session.has_key('userid'):
          del request.session['userid']
      return render(request, 'result.html') 
  ```

## 表单

 Django提供了表单类用来增强表单功能：
增强表单验证：Web应用程序的表单中的输入字段，需要进行验证，“凡有输入，必有验证”。
防止CSRF（Cross Site Request Forgery）攻击,即跨站伪造请求攻击。因为表单可以生成一个CSRF令牌。
方便渲染页面。

Django表单类django.forms.Form和django.forms.ModelForm，Form是普通的表单类，ModelForm是数据库模型对应的表单类。

+ 自定义表单类
  自定义表单类继承django.forms.Form
  from django import forms
  class RegistrationForm(forms.Form):
      ...

+ Form字段类
  CharField：渲染为文本框、密码框和文本域等HTML元素。
  IntegerField：渲染为<input type = 'text'>的HTML元素，只能放置整数。
  DecimalField：渲染为<input type = 'text'>的HTML元素，只能放置小数。
  BooleanField：渲染为<input type = 'checkbox'>的HTML元素。
  ChoiceField：渲染为radio和select等HTML元素。
  DateField：日期字段。
  EmailField：email字段。
  RegexField：正则表达式字段。

+ 示例：

  ```python
  class RegistrationForm(forms.Form):
      username = forms.CharField(label='用户名：', max_length=20)
      email = forms.EmailField(label='邮箱：')
      password1 = forms.CharField(label='密码：', widget=forms.PasswordInput())
      password2 = forms.CharField(label='再次输入密码：', widget=forms.PasswordInput())
      birthday = forms.DateField(label='出生日期：',
                                 error_messages={'invalid': '输入的出生日期无效'})
  ```

```python
def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
        raise forms.ValidationError('两次输入的密码不匹配')
    return password2
```

+ html

  ```html
  <!doctype html>
  {% load static %}
  <html>
  <head>
  <meta charset="utf-8">
  <title>图书管理系统-用户注册</title>
  <link rel="stylesheet" type="text/css" href="{% static 'css/book.css' %}">
  </head>
  
  <body>
  <!-- 页面头部信息 -->
  <div id="header">
      <img src="{% static 'images/book_img2.jpg' %}" width="20px" height="20px">
      用户注册
      <hr/>
  </div>
  <!-- 错误信息 -->
  <ul>
    {% for field,errors in form.errors.items%}
      {% for message in errors%}
      <li class="error">{{ message }}</li>
      {% endfor %}
    {% endfor %}
  </ul>
  <!-- 页面内容信息 -->
  <form action="/books/register",method = "POST">
    {% csrf_token %}
    <div id="content">
      <table width="40%" border="0">
        <tbody>
          <tr>
            <td class="label">{{ form.username.label }}</td>
            <td>{{ form.username }}</td>
          </tr>
          <tr>
            <td class="label">{{ form.password1.label }}</td>
            <td>{{ form.password1 }}</td>
          </tr>
          <tr>
            <td class="label">{{ form.password2.label }}</td>
            <td>{{ form.password2 }}</td>
          </tr>
          <tr>
            <td class="label">{{ form.email.label }}</td>
            <td>{{ form.email }}</td>
          </tr>
          <tr>
            <td class="label">{{ form.birthday.label }}</td>
            <td>{{ form.birthday }}</td>
          </tr>
          <tr align="center">
            <td colspan="2">
              <input type="submit">
              <input type="reset">
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </form>
  
  <!-- 页面底部信息 -->
  <div id="footer">
    <hr/>
    Copyright © 智捷课堂 2008-2018. All Rights Reserved 
  </div>
  
  </body>
  </html>
  
  ```

  

注意：
clean_开头的方法是验证方法，更加复杂的验证，需要在该方法中实现。

用户注册示例：
1、编写表单类
2、编写视图模块
3、编写表单类对应的模板文件
4、显示验证错误信息
5、防止CSRF攻击

## 数据模型

三、定义数据模型
+ 创建用户模型

```python
class User(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True)
    birthday = models.DateField(null=True)
```

```python
# 定义表的元数据
class Meta:
    db_table = 'users'  # 定义表名
    ordering = ['name']  # 设置排序字段
```

+ 自定义模型继承django.db.models.Model类。
+ 字段类型：
  AutoField：自增长字段。
  CharField：可以指定最大值和最小值的字符字段。
  TextField：字符串字段。
  DateField：日期字段。
  DateTimeField：日期时间字段。
  TimeField：时间字段。
  EmailField：email字段。
  IntegerField：整数字段。
  DecimalField：十进制数字段。
  FloatField：浮点数字段。
  ImageField：图片字段。
  https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types

+ 字段可选项：
  null：设置是否字段可以为null。
  blank：设置是否字段可以为空白。
  default：设置默认值。
  primary_key：设置主键。
  unique：设置为候选键。
  https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-options

+ 表的元数据类(Meta)
  在表中定义元数据类Meta，它是一个嵌套类。元数据类Meta的属性：
  db_table：指定表名。
  ordering：设置排序字段。
  abstract：如果设置为True，说明该模型是抽象的，系统不会生成对应的表，它只能作为父类使用。

+ 同步数据库
  模型修改之后，需要执行如下指令：

  > python manage.py makemigrations 
  > python manage.py migrate
  > makemigrations：负责生成数据库迁移计划，生成迁移执行文件。
  > migrate：负责执行或取消数据库迁移。

### 数据的CRUD操作

CRUD就是数据插入（Create）、删除（Delete）、修改（Update）和查询（Read）
测试CRUD操作可以使用manage.py shell命令。

+ 查询所有
  使用User.objects.all()方法，返回的QuerySet集合。

```python
from books.models import User
User.objects.all()
<QuerySet [<User: User object (Tony)>]>
User.objects.all() # 是查询所有数据。QuerySet
```

+ 条件查询
  User.objects.filter()方法返回QuerySet集合。
  User.objects.get()方法返回是模型对象。

  ```python
  from books.models import User
  User.objects.filter(name='Tony')
  <QuerySet [<User: User object (Tony)>]>
  User.objects.get(name='Tony')
  <User: User object (Tony)>
  ```

+ 插入数据

  + 方法1：

    ```python
    User.objects.create() # 方法插入数据 
    User.objects.create(name='关东升',password='123',birthday='1978-5-6')
    <User: User object (关东升)>
    ```

  + 方法2：

    ```python
    # 创建模型对象，调用模型的save()方法实现。
    user = User(name='Tom',password='123',birthday='1977-5-6')
    user.save()
    ```

+ 修改数据

  ```python
  # 先查找模型，修改模型字段，调用模型的save()方法实现。
  u =  User.objects.get(name='Tony')
  u.email = '125@qq.com'
  u.save()
  ```

+ 删除数据

  ```python
  # 先查找模型，调用delete()方法实现。
  u =  User.objects.get(name='Tony')
  u.delete()
  ```

### 数据操作：用户管理案例

+ 查询所有数据

  ```python
  def show_list(request):
      # 查询所有数据
      list = User.objects.all()
      return render(request,"show_list.html",{"list":list})
  ```

+ 插入数据

  ```python
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
  ```

+ 删除数据

  ```python
  def remove_user(request):
      username = request.GET["username"]
      u = User.objects.get(name=username)
      u.delete()
      return HttpResponseRedirect("/books/list/")
  ```

### Q查询

```shell
__exact 精确等于 like ‘aaa’
__iexact 精确等于 忽略大小写 ilike ‘aaa’
__contains 包含 like ‘%aaa%’
__icontains 包含 忽略大小写 ilike ‘%aaa%’，但是对于sqlite来说，contains的作用效果等同于icontains。
__gt 大于
__gte 大于等于
__lt 小于
__lte 小于等于
__in 存在于一个list范围内
__startswith 以…开头
__istartswith 以…开头 忽略大小写
__endswith 以…结尾
__iendswith 以…结尾，忽略大小写
__range 在…范围内
__year 日期字段的年份
__month 日期字段的月份
__day 日期字段的日
__isnull=True/False
```

```python
from django.db.models import Q
# Q(name__startswith='What')
u = User.objects.filter(name__startswith='What')
```

## 通用视图

类基础视图（Class-based views）通常是继承django.views.View。
Django还提供了通用视图类，通用视图类可以与数据库模型绑定，模板命名是固定的。如果使用得当可以大大简化开发过程。通用视图类主要分为：通用显示视图和通用编辑视图。

+ 通用显示视图
  主要用于显示，包括：
  列表视图：django.views.generic.ListView
  详细视图：django.views.generic.DetailView
   这两个视图与数据库模型绑定，而且模板命名是固定的。如果我们的数据模型是User，则模板命名：		user_list.html和user_detail.html，模板存放的位置：

  > books/template/books/user_list.html

### 列表视图

+ views.py

  ```python
  from django.views.generic import ListView
  ...
  class UserListView(ListView):
      model = User
      ordering = ['name']
      queryset = User.objects.filter(name__contains='2')
  ```

+ user_list.html

  ```html
  {% extends "base.html" %}
  {% block title %}用户列表{% endblock %}
  {% block header %}用户列表{% endblock %}
  {% block body %}
  <table width="60%" border="1" align="center">
      <tbody>
      <tr>
          <th width="30%">用户名</th>
          <th width="30%">邮箱</th>
          <th>操作</th>
      </tr>
  
      {% for row in user_list %}
      <tr>
          <td>{{ row.name }}</td>
          <td>{{ row.email }}</td>
          <td>
              <a href="#">修改</a>
              <a href="/books/del/?username={{ row.name }}">删除</a>
          </td>
      </tr>
      {% endfor %}
      </tbody>
  </table>
  {% endblock %}
  ```

### 详细视图

+ views.py

  ```python
  class UserDetailView(DetailView):
      model = User
  ```

+ urls.py

  ```python
  urlpatterns = [
    path("detail/<str:pk>",views.UserDetailView.as_view(),name="detail_view")
  ]
  ```

+ html

  ```html
  <!doctype html>
  {% load static %}
  <html>
  <head>
  <meta charset="utf-8">
  <title>图书管理系统-用户注册</title>
  <link rel="stylesheet" type="text/css" href="{% static 'css/book.css' %}">
  </head>
  
  <body>
  <!-- 页面头部信息 -->
  <div id="header">
      <img src="{% static 'images/book_img2.jpg' %}" width="20px" height="20px">
      用户注册
      <hr/>
  </div>
  
  <!-- 页面内容信息 -->
  
    <div id="content">
      <table width="40%" border="0">
        <tbody>
          <tr>
            <td class="label">用户名:</td>
            <td>{{ user.name }}</td>
          </tr>
          <tr>
            <td class="label">密码:</td>
            <td>{{ user.password }}</td>
          </tr>
          <tr>
            <td class="label">邮箱:</td>
            <td>{{ user.email }}</td>
          </tr>
          <tr>
            <td class="label">出生日期:</td>
            <td>{{ user.birthday|date:"Y-m-d" }}</td>
          </tr>
          <tr align="center">
            <td colspan="2">
              <input type="button" value="返回" onclick="window.history.go(-1)">
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  
  
  <!-- 页面底部信息 -->
  <div id="footer">
    <hr/>
    Copyright ©  2008-2018. All Rights Reserved 
  </div>
  
  </body>
  </html>
  
  ```

### 分页视图

+ views.py

  ```python
  class UserListView(ListView):
      model = User
      ordering = ["name"]
      paginate_by = 1  # 每页页数
      # queryset = User.objects.filter(name__contains="tom")
  ```

+ html

  ```html
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  
  <div align="right">
  {% if is_paginated %}
    <ul class="pagination">
      {% if page_obj.has_previous %}
        <li><a href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
      {% else %}
        <li class="disabled"><span>&laquo;</span></li>
      {% endif %}
      {% for i in paginator.page_range %}
        {% if page_obj.number == i %}
          <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
        {% else %}
          <li><a href="?page={{ i }}">{{ i }}</a></li>
        {% endif %}
      {% endfor %}
      {% if page_obj.has_next %}
        <li><a href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
      {% else %}
        <li class="disabled"><span>&raquo;</span></li>
      {% endif %}
    </ul>
  {% endif %}
  </div>
  ```

### 编辑视图

## 文件上传

+ views.py

  ```python
  def upload(request):
      if request.method == "POST":
          form = UploadFileForm(request.POST,request.FILES)
          if form.is_valid():
              handle_uploaded_file(request.FILES["file"])
              return HttpResponse("<h5>文件上传成功</h5>")
      else:
          form = UploadFileForm()
  
      return render(request,"upload.html",{"form":form})
  
  
  def handle_uploaded_file(f):
      path = "upload/" + f.name
      with open(path,"wb+") as destination:
          for chunk in f.chunks():
              destination.write(chunk)
  ```

+ forms.py

  ```python
  class UploadFileForm(forms.Form):
      file = forms.FileField()
  ```

+ upload.html

  ```python
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>上传文件</title>
  </head>
  <body>
      <form action="/books/upload/" method="POST"
            enctype="multipart/form-data">
          {% csrf_token %}
        <input type="file" name="file"><br><br>
        <input type="submit" name="开始上传">
      </form>
  </body>
  </html>
  ```

## 发送邮件












