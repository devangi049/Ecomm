from django.db import models
from EcommApp.models.user import User


class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.fname}'s Cart"


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey("Product",on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs"
    
    

