from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Product(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(verbose_name="Qiymət")
    weight = models.PositiveIntegerField()
    order_date = models.DateField()
    delivered = models.BooleanField(verbose_name="Bakıya çatdırılma")


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
