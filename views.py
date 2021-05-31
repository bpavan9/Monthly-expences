from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from .models import Book,Employee,Order
from .serializers import BookSerializer,EmployeeSerializer,Orderserializer

# Create your views here.
def home(request):
    return render(request,'Test_app/home.html')

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all
    serializer_class = Orderserializer

