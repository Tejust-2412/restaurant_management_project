from django.contrib import admin
from .models import Coupon , Order , OrderStatus
# Register your models here.

@admi.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id' , 'code' , 'discount' , 'created')
    search_fiedls = ('code' ,)
    list_filter = ('created_at' ,)

admin.site.register(OrderStatus)
admin.site.register(Order)