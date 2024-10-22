from django.urls import path,re_path
from . import views


urlpatterns = [
  # path("info1/",views.show_book_info1),
  # path("info2/",views.show_book_info2),
  # path("myview/",views.MyView.as_view(),name = "myview"),
  # path("price/<int:price>",views.show_book_price1,name = "book_price1"),
  # re_path("^price/(?P<price>\d+\.\d+)/$",views.show_book_price2,name = "book_price2"),
  # path("",views.show_book_info,name = "show_book_info"), 
  path("login/",views.login,name = "login"),
  path("register/",views.RegisrationFormView.as_view(),name = "register_view"),
  path("list/",views.UserListView.as_view(),name = "userList"),
  path("del/<str:pk>",views.UserDeleteView.as_view(),name = "delete_user"),
  path("detail/<str:pk>",views.UserDetailView.as_view(),name="detail_view"),
  path("upload/",views.upload,name = "upload"),
  # path("hello/",views.hello,name = "hello")
]