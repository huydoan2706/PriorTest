from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Receipt(models.Model):
    receipt_date = models.DateField(default=timezone.now)
    supplier_name = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receipt", null=True)

    def __str__(self):
        return f"The receipt {self.id} is supplied by {self.supplier_name} on {self.receipt_date}"


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField(default=1)
    description = models.TextField()
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.quantity} - {self.price} VND - {self.receipt.id}"
