from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_statuses(sender , **kwargs) :
    from .models import OrderStatus
    from .import  ORDER_STATUSES
    for status in ORDER_STATUSES :
        OrderStatus.objects.get_or_create(name=status)


    


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'


