from django.db import models

# Create your models here.
class MenuCategory (models,Model):
    name = models.CharFied(max_length = 100 , unique = True )


    class Meta :
        verbose_name_plural = "Menu Categories"

    def __str__(self):
        return self.name 



class MenuItem(models.Model):
    name = models.CharField(max_length = 200 )
    description = models.TextField(blank = True , null = True )
    price = models.DecimalField(max_digits = 8 , decimal_places = 2)
    available = models.BooleanField(default = True)
    category = models.ForeignKey(MenuCategory , on_delete = models.CASCADE , related_name = "items")


    def __str__(self) :
        return self.name