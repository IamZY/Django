from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("register/",views.register,name = "register"),
    path("login/",views.login,name = "login"),
    path("main/",views.main,name = "main"),
    path("list/",views.GoodsListView.as_view(),name = "list"),
    path("detail/",views.show_goods_detail,name = "detail"),
    path("add/",views.add_cart),
    path("show_cart/",views.show_cart),
    path("submit_orders/",views.submit_orders),
    path("logout/",views.logout)
]
