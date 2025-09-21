from django.db import models
from django.contrib.auth.models import User
from .models import OrderStatus 
# Create your models here.
class Order(models.Model):
    customer = models.ForeighnKey(User , on_dekete = models.CASCADE)
    product = models.CharField(max_length = 100)
    quantity = models.PositiveIntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add = True)

    status = models.ForeighKey(
        OrderStatus , 
        on_delete = models.SET_NULL , 
        null = True , 
        blank = True ,
        related_name = "orders"
    )

    def __str__(self) :
        return f"Order #{self.id} - {self.product} ({self.status})"


class OrderStatus(models..Model):
    name = models.CharField(max_length = 50 , unique = True)


    class Meta :
        verbose_name_plural = "Order Statuses"


    def __str__(self):
        return self.name


class Coupon(models.Model) :
    code = models.CharFied(max_lenth = 20 , unique = True)
    discount = models.DescimalField(max_lenth = 5 , decimal_places = 2 )
    discount = models.DescimalField(max_digith = 5  , decimal_places= 2)
    created_at = models.DateTimeField (auto_now_add = True)


    def __str__(self):
        return self.code