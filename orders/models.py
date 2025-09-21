from django.db import models

# Create your models here.
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