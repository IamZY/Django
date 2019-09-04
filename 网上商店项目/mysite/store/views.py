from django.shortcuts import render,HttpResponseRedirect
from .forms import RegistrationForm,LoginForm
from .models import Customer, Goods, OrderLineItem, Orders
from django.views.generic import ListView,DetailView
import random
import datetime

# Create your views here.

# 登录
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password']
            c = Customer.objects.get(id=userid)

            if c is not None and c.password == password:
                # 客户id放到HTTP Session中
                request.session['customer_id'] = c.id
                return HttpResponseRedirect('/main/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_customer = Customer()
            new_customer.id = form.cleaned_data["userid"]
            new_customer.name = form.cleaned_data["name"]
            new_customer.password = form.cleaned_data["password1"]
            new_customer.birthday = form.cleaned_data["birthday"]
            new_customer.phone = form.cleaned_data["phone"]

            new_customer.save()

            return render(request, "customer_reg_success.html")
    else:
        form = RegistrationForm()

    return render(request, "customer_reg.html", {"form": form})


def main(request):
    # 判断客户是否已经登录
    if not request.session.has_key('customer_id'):
        print('没有登录')
        # 重新登录
        return HttpResponseRedirect('/login/')

    return render(request, 'main.html')



class GoodsListView(ListView):
    model = Goods
    ordering = ["id"]
    # queryset =
    template_name = "goods_list.html"


def show_goods_detail(request):
    goodid = request.GET["id"]
    # print(goodid+'--')
    goods = Goods.objects.get(id=goodid)
    return render(request,"goods_detail.html",{"goods":goods})


# 添加购物车
def add_cart(request):
    # 判断客户是否已经登录
    if not request.session.has_key('customer_id'):
        print('没有登录')
        # 重新登录
        return HttpResponseRedirect('/login/')

    goodsid = int(request.GET['id'])
    goodsname = request.GET['name']
    goodsprice = float(request.GET['price'])

    # 判断Session中是否已经存在购物车数据
    if not request.session.has_key('cart'):
        # 如果没有则创建一个空购物车,购物车是列表结构
        request.session['cart'] = []

    cart = request.session['cart']

    flag = 0  # 声明一个标志,0表示购物车中没有当前商品,1表示购物车中有当前商品
    for item in cart:
        # item也是列表结构,例如:[商品id, 商品名称, 价格, 数量]
        if item[0] == goodsid:  # 当前商品购物车有
            item[3] += 1
            flag = 1
            break

    if flag == 0:  # 当前商品购物车没有
        item = [goodsid, goodsname, goodsprice, 1]
        cart.append(item)

    request.session['cart'] = cart

    print(cart)

    page = request.GET['page']
    if page == 'detail':
        return HttpResponseRedirect('/detail/?id=' + str(goodsid))
    else:
        return HttpResponseRedirect('/list/')


def show_cart(request):
    # 判断客户是否已经登录
    if not request.session.has_key('customer_id'):
        print('没有登录')
        # 重新登录
        return HttpResponseRedirect('/login/')

    if not request.session.has_key('cart'):
        print('购物车是空的')
        return render(request, 'cart.html', {'list': [], 'total': 0.0})

    cart = request.session['cart']
    list = []
    total = 0.0
    for item in cart:
        # item 结构 [商品id, 商品名称, 价格, 数量]
        # 计算小计
        subtotal = item[2] * item[3]
        total += subtotal
        # 追加小计到 new_item (商品id, 商品名称, 价格, 数量, 小计)
        new_item = (item[0], item[1], item[2], item[3], subtotal)

        list.append(new_item)

    return render(request, 'cart.html', {'list': list, 'total': total})

def submit_orders(request):
    if request.method == 'POST':
        # 从表单上取出数据添加到Orders模型对象
        orders = Orders()
        # 生成订单id,规则是当前时间戳+1位随机数
        n = random.randint(0, 9)
        d = datetime.datetime.today()
        ordersid = str(int(d.timestamp() * 1e6)) + str(n)
        orders.id = ordersid
        orders.order_date = d
        orders.status = 1
        orders.total = 0.0

        orders.save()

        cart = request.session['cart']
        total = 0.0

        for item in cart:
            # item 结构 [商品id, 商品名称, 价格, 数量]
            # 商品id
            goodsid = item[0]
            goods = Goods.objects.get(id=goodsid)

            quantity = request.POST['quantity_' + str(goodsid)]

            try:
                quantity = int(quantity)
            except:
                quantity = 0

            # 计算小计
            subtotal = item[2] * quantity
            total += subtotal

            order_line_item = OrderLineItem()
            order_line_item.quantity = quantity
            order_line_item.goods = goods
            order_line_item.orders = orders
            order_line_item.sub_total = subtotal

            order_line_item.save()

        orders.total = total
        orders.save()

        # 提交订单后购物车应该清除
        del request.session['cart']

        return render(request, 'order_finish.html', {'ordersid': ordersid})


def logout(request):
    if request.session.has_key('customer_id'):
        del request.session['customer_id']
        if request.session.has_key('cart'):
            del request.session['cart']

    return HttpResponseRedirect('/login/')
