from .models import Order
from product.models import Product
from rest_framework import serializers


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'type_product', 'price')


class OrderSerializer(serializers.ModelSerializer):
    products = ProductItemSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Order
        fields = ('id', 'name_client', 'status', 'products', 'amount')
