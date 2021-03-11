from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)