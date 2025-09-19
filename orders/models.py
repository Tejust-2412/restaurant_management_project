from django.db import models

# Create your models here.


class Coupon(models.Model) :
    code = models.CharFied(max_lenth = 20 , unique = True)
    discount = models.DescimalField(max_lenth = 5 , decimal_places = 2 )
    discount = models.DescimalField(max_digith = 5  , decimal_places= 2)
    created_at = models.DateTimeField (auto_now_add = True)


    def __str__(self):
        reeturn self.code