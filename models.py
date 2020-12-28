from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Catgeory(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(default=0.0)
    date=models.DateField(default=timezone.now)
    catgeory=models.ForeignKey(Catgeory,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Wallet(models.Model):
    credit_amount=models.IntegerField(default=0)
    debit_amount=models.IntegerField(default=0)
    transaction_date=models.DateField(default=timezone.now)


class Wallet_balance(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    purchased_iteamname=models.CharField(max_length=30)
    purchased_iteam_date = models.DateField()
    purchaseiteam_price=models.FloatField(default=0.0)
    wallet_debit_amount=models.IntegerField(default=0)
    wallet_credit_amount=models.IntegerField(default=0)
    wallet_transaction_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username






