from django.db import models

# Create your models here.
# 创建客户模型
class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=20)
    address = models.CharField(null=True, max_length=100)
    phone = models.CharField(null=True, max_length=20)
    birthday = models.DateField(null=True)

    # 定义表的元数据
    class Meta:
        db_table = 'Customers'  # 定义表名
        ordering = ['id']  # 设置排序字段


# 创建商品模型
class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)
    price = models.FloatField()
    description = models.CharField(null=True, max_length=200)
    brand = models.CharField(null=True, max_length=30)
    cpu_brand = models.CharField(null=True, max_length=30)
    cpu_type = models.CharField(null=True, max_length=30)
    memory_capacity = models.CharField(null=True, max_length=30)
    hd_capacity = models.CharField(null=True, max_length=30)
    card_model = models.CharField(null=True, max_length=30)
    displaysize = models.CharField(null=True, max_length=30)
    image = models.CharField(null=True, max_length=100)

    # 定义表的元数据
    class Meta:
        db_table = 'Goods'  # 定义表名
        ordering = ['id']  # 设置排序字段


# 创建订单模型
class Orders(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    order_date = models.DateTimeField()
    status = models.IntegerField(default=1)
    total = models.FloatField()

    # 定义表的元数据
    class Meta:
        db_table = 'Orders'  # 定义表名
        ordering = ['order_date']  # 设置排序字段


# 创建订单详细模型
class OrderLineItem(models.Model):
    id = models.AutoField(primary_key=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    sub_total = models.FloatField(default=0.0)

    # 定义表的元数据
    class Meta:
        db_table = 'OrderLineItems'  # 定义表名
        ordering = ['id']  # 设置排序字段
