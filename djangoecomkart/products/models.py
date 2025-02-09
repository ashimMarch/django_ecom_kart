from django.db import models

# Create your models here.
# Ratheeshts/brokart.git
# Models for Product
class Product(models.Model) :
    LIVE=0
    DELETE=1
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))

    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title