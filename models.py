from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=64,blank=True)
    author=models.CharField(max_length=64,blank=True)
    publisher=models.CharField(max_length=64,blank=True)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname=models.CharField(max_length=64)
    emp_code=models.CharField(max_length=64)
    mobile=models.IntegerField(max_length=64)


class Order(models.Model):
    product=models.CharField(max_length=64)
    customer=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    date=models.DateField()
