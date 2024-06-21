from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class salama_register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=30)
    phone_number = models.IntegerField()
    route = models.CharField(max_length=60)

    class Meta:
        db_table = 'salama_customers'


class OrderForm(models.Model):
    item = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    route = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'salama_orders'
        # ordering = ['item', 'description', 'quantity', 'route']
