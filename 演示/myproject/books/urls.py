from django.urls import path
from . import views


urlpatterns = [
    path("hello/",views.hello,name = "hello"),
    path("myview/",views.MyView.as_view(),name = "myview")
]