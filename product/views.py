from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)
