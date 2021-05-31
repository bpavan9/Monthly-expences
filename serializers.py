from rest_framework import serializers
from .models import Book,Employee,Order

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['title']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields='__all__'

class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields='__all__'



