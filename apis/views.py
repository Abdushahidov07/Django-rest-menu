from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


class DishListAPIView(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['name_dish',"prf_time", "time_category"] 
    search_fields = ['name_dish',"time_category"]

class DishCreateAPIView(CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishDestroyAPIView(DestroyAPIView):
    queryset = Dish.objects.all()

class TableListAPIView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['type',"max_person",] 
    search_fields = ['type',]

class TableCreateAPIView(CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDestroyAPIView(DestroyAPIView):
    queryset = Table.objects.all()




class BillListAPIView(ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['table',"castumername",] 
    search_fields = ['castumername',]

class BillCreateAPIView(CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDestroyAPIView(DestroyAPIView):
    queryset = Bill.objects.all()


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['dish',"bill",] 
    search_fields = ['id',]

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDestroyAPIView(DestroyAPIView):
    queryset = Order.objects.all()