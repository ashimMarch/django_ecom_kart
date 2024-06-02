from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.


# Models for Order
class Order(models.Model):
    LIVE=0
    DELETE=1
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_CONFIRMED,"ORDER_PROCESSED"),(ORDER_DELIVERED,"ORDER_DELIVERED"),(ORDER_REJECTED,"ORDER_REJECTED"))
    
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title

# model for OrderedItem
class OrderedItem(models.Model):
   product=models.ForeignKey(Product, related_name='added_carts',on_delete=models.SET_NULL,null=True) 
   quanity=models.IntegerField(default=1)
   owner=models.ForeignKey(Order, on_delete=models.CASCADE,related_name='added_items')
   